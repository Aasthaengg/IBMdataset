import sys
readline = sys.stdin.readline

N = int(readline())
V = sorted(list(map(int,readline().split())))

ans = V[0]
for i in range(1,len(V)):
  ans = (ans + V[i]) / 2
  
print(ans)
