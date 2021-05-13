import sys
n = int(input())
t,a = map(int,input().split())
h = list(map(int,input().split()))

near = sys.maxsize
ans = 0

for i in range(n):
  if abs(a - (t-h[i]*0.006)) < near:
    ans = i+1
    near = abs(a - (t-h[i]*0.006))

print(ans)