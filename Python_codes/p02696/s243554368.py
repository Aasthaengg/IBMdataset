A, B, N = map(int, input().split())
x = N

if N >= B - 1:
  x = B - 1

ans = A*x//B - A*(x//B)
  
print(ans)