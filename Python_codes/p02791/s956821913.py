N=int(input())
P=list(map(int,input().split()))
INF=10**10
count = 1
MIN=P[0]
for i in range(1,N):
  if P[i] <= MIN:
    MIN=P[i]
    count += 1
print(count)