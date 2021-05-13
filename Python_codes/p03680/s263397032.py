n = int(input())
a = []
for _ in range(n):
  a_ = int(input())
  a.append(a_)

ans = 0
c = 1
for i in range(n):
  c = a[c-1]
  ans += 1
  if c == 2:
    print(ans)
    exit()
print(-1)