N = int(input())

ans = 0
for i in range(N):
  if ((i+1) % 3) == 0:
    continue
  elif ((i+1) % 5) == 0:
    continue
  ans += i+1

print(ans)