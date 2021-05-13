n = int(input())
sn = {}
for _ in range(n):
  s = input()
  if not s in sn:
    sn[s] = 1
  else :
    sn[s] += 1

m = int(input())
tn = {}
for _ in range(m):
  t = input()
  if not t in tn:
    tn[t] = 1
  else :
    tn[t] += 1

answer = 0
for skey in sn.keys():
  if not skey in tn:
    check = sn[skey]
  else :
    check = sn[skey] - tn[skey]
  if answer < check:
    answer = check

print(answer)