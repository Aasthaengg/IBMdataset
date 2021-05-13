x,y = [int(hoge) for hoge in input().split()]
if x==y:print(0);exit()
#K回…
#押して反転 or 反転して押す or 反転押して反転
#-x-K or -x + K or x + k or x-k
kouho =  [-x-y+1,x+y+1,y-x,x-y+2]
print(min([k for k in kouho if k>0]))