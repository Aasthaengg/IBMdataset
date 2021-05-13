K,X = map(int,input().split())
A = []

for n in range(X-K+1,X+K):
  A.append(n)

print(*A)