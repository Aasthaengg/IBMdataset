a,b,m = map(int,input().split())

A = list(map(int,input().split()))
B = list(map(int,input().split()))

ans = min(A)+min(B)

for i in range(m):
  x,y,c = map(int,input().split())
  cost = A[x-1] + B[y-1] - c
  if cost < ans:
    ans = cost

print(ans)    