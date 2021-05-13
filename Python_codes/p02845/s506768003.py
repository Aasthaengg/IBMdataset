import collections

mod=10**9+7
n=int(input())
arr=list(map(int,input().split()))
dic=collections.defaultdict(int)
dic[-1]=3
ans=1
for i in range(n):
  dic[arr[i]]+=1
  ans*=dic[arr[i]-1]
  ans%=mod
  dic[arr[i]-1]-=1
print(ans)    