N, L = map(int, input().split())
s = []
for i in range(N):
  s.append(i+L)
t = list(map(abs, s))
del s[t.index(min(t))]
print(sum(s))