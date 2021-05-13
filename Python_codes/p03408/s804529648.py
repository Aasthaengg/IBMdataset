n = int(input())
s = [input() for i in range(n)]
m = int(input())
t = [input() for j in range(m)]
S = list(set(s))
T = list(set(t))
b = []

for x in range(len(S)):
  a = s.count(S[x]) - t.count(S[x])
  b.append(a)
ans = max(0, max(b))
print(ans)