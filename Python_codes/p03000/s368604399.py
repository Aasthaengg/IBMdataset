import itertools
n,x=map(int,input().split())
l=list(map(int,input().split()))
cumsum=[0]+list(itertools.accumulate(l)) # 累積和
cnt=0
for c in cumsum:
    if c<=x:
        cnt+=1
print(cnt)