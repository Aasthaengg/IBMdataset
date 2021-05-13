N = int(input()); INF = float("inf")
A = INF
for i in range(N):
  a,b = map(int,input().split())
  A = min(A,(a+b))
print(A)