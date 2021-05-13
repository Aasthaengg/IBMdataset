N = int(input())
A = list(map(int, input().split()))
INF = 10**9

dp0 = [0]
dp1 = [-INF-1]

for i, x in enumerate(A):
  dp0.append( max(dp0[i] + x, dp1[i] - x) )
  dp1.append( max(dp0[i] - x, dp1[i] + x) )

print(dp0[-1])
