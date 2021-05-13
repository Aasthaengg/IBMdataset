N = int(input())
ans = 0

Ru = int(N**0.5)

for i in range(N):
  ans += N//(i+1)
  if N%(i+1)==0:
    ans -= 1

print(ans)