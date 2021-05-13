import sys
readline = sys.stdin.readline

N = int(readline())

p = 0
ans = set()
for i in range(1,N + 1):
  p += i
  ans.add(i)
  if p >= N:
    break
    
if p == N:
  for a in ans:
    print(a)
  exit(0)
ans.remove(p - N)
for a in ans:
  print(a)
