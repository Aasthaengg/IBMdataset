n,m = list(map(int,input().split()))
d = {}
ac = 0
wa = [0] * (n+1)
wa_sum = 0

for i in range(m):
  p,s = input().split()
  p = int(p)
  if p in d:
    if d[p] == 'AC':
      pass
    else:
      if s == 'AC':
        d[p] = 'AC'
        ac += 1
        wa_sum += wa[p]
      else:
        wa[p] += 1
  else:
    d[p] = s
    if s == 'AC':
      ac += 1
    else:
      wa[p] += 1

print(ac,wa_sum)