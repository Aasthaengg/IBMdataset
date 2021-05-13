n, m = map(int, input().split())
s = input()[::-1]
now = 0
L = []
while now<n:
  t = s[now:now+m+1].rfind("0")
  if t==0:
    print(-1)
    exit()
  else:
    L.append(t)
    now += t
print(*L[::-1])