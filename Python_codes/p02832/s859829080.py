n = int(input())

B = list(map(int, input().split()))

nxt = 1
broken = 0
for i in range(n):
  if B[i]==nxt:
    nxt += 1
  else:
    broken += 1
    
if broken==n:
  print(-1)
else:
  print(broken)
