T = [int(input()) for _ in range(5)]
T.sort(key=lambda x:x % 10 if x % 10 != 0 else 10)

ans = 0
ans += T[0]
for i in range(1,5):
  ans += T[i]
  if T[i] % 10 != 0:
    ans += 10 - T[i] % 10
print(ans)
