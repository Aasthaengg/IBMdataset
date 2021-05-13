N = int(input())
S = [int(input()) for i in range(N)]
s_10 = []
s_other = []
for s in S:
  if s % 10:
    s_other.append(s)
  else:
    s_10.append(s)

s_other.sort()
ans = sum(S)
other_mod_10 = sum(s_other) % 10
if s_other:
  if other_mod_10:
    print(ans)
  else:
    print(ans - min(s_other))
else:
  print(0)