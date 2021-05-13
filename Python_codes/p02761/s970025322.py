n, m = map(int,input().split())
s = []
c = []
for _ in range(m):
  x, y = map(int,input().split())
  s.append(x)
  c.append(y)

for i in range(10 ** (n + 1)):
    Str = str(i)

    if len(Str) == n and all([Str[s[j] - 1] == str(c[j]) for j in range(m)]):
        print(Str)
        exit()

print(-1)
