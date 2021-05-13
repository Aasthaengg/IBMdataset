#k回消化コストを-1できる

n,k=map(int,input().split())
#消化コスト
a=list(map(int,input().split()))
a.sort()
#食べにくさ
f=list(map(int,input().split()))
f.sort(reverse=True)

#食べやすいものを消化コストが高い人
#食べにくいものを消化コストが低い人にしたほうがいい
#kをどこで減らすかは2部探索
#a-ans//f の和がk以下で、最小のans

ll=-1
rr=10**18

result=10**18
while ll+1<rr:
    ans=(rr+ll)//2
    
    cnt=0
    for i in range(n):
        cnt+=max(0,a[i]-ans//f[i])
    if cnt<=k:
        rr=ans
    else:
        ll=ans
#ansが小さくなると、cntが大きくなる



print(rr)


    



