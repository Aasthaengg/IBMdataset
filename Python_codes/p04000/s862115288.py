h,w,n=map(int,input().split())
dic={}
dx=[-2,-1,0]
dy=[-2,-1,0]
ans=[0]*10
for _ in range(n):
  a,b=map(int,input().split())
  for x in dx:
    for y in dy:
      if 1<=a+y and a+y+2<=h and 1<=b+x and b+x+2<=w:
        if (a+y,b+x) not in dic:
          dic[(a+y,b+x)]=1
        else:
          dic[(a+y,b+x)]+=1
ans[0]=(h-2)*(w-2)-len(dic)
for v in dic.values():
  ans[v]+=1
for i in range(10):
  print(ans[i])
