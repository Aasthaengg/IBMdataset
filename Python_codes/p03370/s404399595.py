N, X = map(int, input().split())
m = [int(input()) for i in range(N)]

ans = N
for i in m:
  X -= i
  
ans += X // min(m)

print(ans)