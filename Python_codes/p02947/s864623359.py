N = int(input())
s = []
for i in range(N):
  tmp = list(input())
  tmp.sort()
  s.append("".join(tmp))

s.sort()
m = {}
for i in range(len(s)):
  if s[i] in m.keys():
    m[s[i]] += 1
  else:
    m[s[i]] = 1

v = [int(x * (x-1) / 2) for x in list(m.values())]
print(sum(v))
