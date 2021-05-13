N = int(input())
A = list(map(int,input().split()))
A.sort()
M = A[-1]+1
DP = [0]*M
for i in A:
  DP[i] += 1
  for j in range(i*2,M,i):
    DP[j] = 2
print(DP.count(1))