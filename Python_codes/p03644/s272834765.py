n = int(input())
ans = 0
for i in range(8):
  if 2**i <= n:
    ans=2**i
print(ans)