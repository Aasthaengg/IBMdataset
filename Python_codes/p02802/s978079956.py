n, m = map(int, input().split())

ac_cnt = 0
wa_cnt = 0
d = {}

for _ in range(m):
  p, s = input().split()
  if p not in d:
    d[p] = [s]
  else:
    d[p].append(s)
    
for i in d:
  if 'AC' in d[i]:
    ac_cnt += 1
    wa_cnt += d[i].index('AC')
print(ac_cnt, wa_cnt)