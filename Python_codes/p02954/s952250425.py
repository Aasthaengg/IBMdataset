S = input()
S += 'R'

ans = [0]*(len(S))
rcnt = 0
lcnt = 0
l = 0
pre = 'R'
for i, s in enumerate(S):
  if s == 'R':
    rcnt += 1
    if pre == 'L':
      ans[l-1] += lcnt//2
      ans[l] += (lcnt+1)//2
      lcnt = 0
  else:
    lcnt += 1
    if pre == 'R':
      l = i
      ans[i-1] = (rcnt+1)//2
      ans[i] += rcnt//2
      rcnt = 0
  pre = s
print(*ans[:-1])