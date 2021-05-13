d = {}
n = int(input())
for _ in range(n):
  s = input()
  if s in d: d[s] += 1
  else: d[s] = 1

m = int(input())
for _ in range(m):
  t = input()
  if t in d: d[t] -= 1
    
maxNum = max(d.values())
if maxNum > 0: print(maxNum)
else: print(0)