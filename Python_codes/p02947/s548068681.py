from collections import Counter
N = int(input())
d = dict()

ans = 0
for i in range(N):
  s = str(input())
  s = ''.join(sorted(s))
  if s in d:
    ans += int(d[s])
    d[s] = int(d[s]) + 1
  else:
    d[s] = 1
    
print(ans)