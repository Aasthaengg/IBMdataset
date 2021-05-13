import itertools
n = int(input())
d = {'M': 0, 'A': 0, 'R': 0, 'C': 0, 'H': 0}
for i in range(n):
  s = input()
  if s[0] in d:
    d[s[0]] += 1
ans = 0
for v in itertools.combinations(d, 3):
    ans += d[v[0]] * d[v[1]] * d[v[2]]
print(ans)