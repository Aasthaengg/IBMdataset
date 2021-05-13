import sys

n = int(sys.stdin.readline())
A = [int(x) for x in sys.stdin.readline().split()]
q = int(sys.stdin.readline())
Qs = [int(x) for x in sys.stdin.readline().split()]

l = len(A)
N = 2000
dp = [False] * (N+1)
dp[0] = True

for a in A:
    tmp = dp.copy()
    for j in range(N+1):
        if j + a > N:break

        if tmp[j]:
            dp[j+a] = True

for m in Qs:
    if dp[m]:
        print("yes")
    else:
        print("no")
