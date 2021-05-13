n = int(input())
a = [int(input()) for i in range(n)]
ans = 0
now = -1
for i in a:
  if i > now + 1:
    print(-1)
    exit()
  elif i < now + 1:
    ans += now
  now = i
ans += now
print(ans)