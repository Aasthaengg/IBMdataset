S,K=list(map(int, input().split()))
H=[]
for _ in range(S):
  H.append(int(input()))
H.sort()
INF=float('inf')
a=[INF]*(S-K+1)
for i in range(S-K+1):
  a[i]=H[i+K-1]-H[i]
print(min(a))