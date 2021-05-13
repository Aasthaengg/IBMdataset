N = int(input())
V = sorted(map(int,input().split()))
ans = V[0]

for v in V:
  ans=(ans+v)/2

print(ans)