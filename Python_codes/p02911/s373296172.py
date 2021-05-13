from collections import Counter
n,k,q=map(int,input().split())
a=[int(input()) for _ in range(q)]

cnt=Counter(a)

ans=['No' if k-q<=0 else 'Yes']*(n+1)

for key,value in cnt.items():
    if k-q+value>0:
        ans[key]='Yes'

for i in range(1,n+1):
    print(ans[i])