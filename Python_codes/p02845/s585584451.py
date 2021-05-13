n=int(input())
a=list(map(int,input().split()))
cnt_num=[0]*(n+1)
cnt_num[0]=3
ans=1
p=10**9+7
for i in range(n):
  ans *= cnt_num[a[i]]
  ans %=p
  cnt_num[a[i]+1]+=1
  cnt_num[a[i]]-=1
print(ans%p)