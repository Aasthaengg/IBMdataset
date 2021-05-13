n = input()
p = list(map(int,input().split()))

ps = sorted(p)

d_p = []
d_ps = []
for i,q in enumerate(p):
  if q != ps[i]:
    d_p.append(q)
    d_ps.append(ps[i])
if len(d_p) > 2:
  print('NO')
elif len(d_p) == 2:
  d_p.sort()
  if d_p == d_ps:
    print('YES')
  else:
    print('NO')
else:
  print('YES')