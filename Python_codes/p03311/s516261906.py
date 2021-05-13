import copy
N=int(input())
lst=list(map(int,input().split()))
lst2=copy.copy(lst)
for i in range(1,N+1):
  lst2[i-1]-=i
lst2=sorted(lst2)
b=lst2[N//2]
ans=0
for i in range(N):
  ans+=abs(lst[i]-(b+i+1))
print(ans)