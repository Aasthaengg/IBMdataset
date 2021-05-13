N = int(input())
ans = 0
for i in range(N):
  if 2**i <= N:
    ans = 2**i
    
print(ans)