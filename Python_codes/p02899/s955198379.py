n = int(input())
l = list(map(int, input().split()))
c = {}
for i in range(n):
  c[l[i]] = i + 1
c = sorted(c.items())
[print(s[1], end=" ") for s in c]
