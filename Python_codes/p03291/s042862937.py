#22:24
s = input()
mod = 10 ** 9 + 7
cum = [[0],[0],[0],[0]]
for i in range(len(s)):
  tmp = ord(s[i]) - 65
  if tmp == -2:
    tmp = 3
  for j in range(4):
    if j == tmp:
      cum[j].append(cum[j][-1]+1)
    else:
      cum[j].append(cum[j][-1])
q = cum[3][-1]
tri = [1]
for _ in range(len(s)):
  tri.append(tri[-1] * 3 % mod)
ans = 0
for i in range(len(s)):
  if s[i] == 'B':
    ans += cum[0][i] * (cum[2][-1]-cum[2][i+1]) * tri[q]
    ans += cum[0][i] * (cum[3][-1]-cum[3][i+1]) * tri[q-1]
    ans += cum[3][i] * (cum[2][-1]-cum[2][i+1]) * tri[q-1]
    ans += cum[3][i] * (cum[3][-1]-cum[3][i+1]) * tri[q-2]
  if s[i] == '?':
    ans += cum[0][i] * (cum[2][-1]-cum[2][i+1]) * tri[q-1]
    ans += cum[0][i] * (cum[3][-1]-cum[3][i+1]) * tri[q-2]
    ans += cum[3][i] * (cum[2][-1]-cum[2][i+1]) * tri[q-2]
    ans += cum[3][i] * (cum[3][-1]-cum[3][i+1]) * tri[q-3]
  ans %= mod
print(ans)