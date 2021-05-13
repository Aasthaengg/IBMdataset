import collections

N,K=map(int,input().split())
A=list(map(int,input().split()))

check=collections.Counter(A).most_common()
ans=0
for i in range(K,len(check)):
  ans+=check[i][1]
print(ans)
