# -*- coding: utf-8 -*-

N, M = map(int, input().split())
s = []
c = []
for i in range(M):
  si, ci = map(int, input().split())
  s.append(si)
  c.append(ci)

# x[0]は1の位、x[1]は10の位、x[2]は100の位
x = [-1] * N

for i in range(M):
  
  if N > 1 and s[i] == 1 and c[i] == 0:
    print(-1)
    exit()
  
  if x[N - s[i]] == -1 or x[N - s[i]] == c[i]:
    x[N - s[i]] = c[i]
  else:
    print(-1)
    exit()

if N == 1 and x[0] == -1:
  x[0] = 0
    
if x[N-1] == -1:
  x[N-1] = 1
for i in range(N-1):
   if x[i] == -1:
      x[i] = 0

ans = 0
for i in range(N):
  ans += x[i] * (10**i)

print(ans)