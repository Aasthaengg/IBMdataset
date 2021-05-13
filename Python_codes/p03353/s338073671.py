s = input()
K = int(input())
d = list()
for l in range(len(s)):
  for r in range(l,min(l+K+1, len(s))):#左からl番目、右からr番目までの文字列
    n = s[l:r+1]
    if n not in d:
      d.append(n)
    d.sort()
    d = d[:5]
print(d[K-1])

