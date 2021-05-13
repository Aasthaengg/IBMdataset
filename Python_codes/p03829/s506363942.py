import sys
input = sys.stdin.readline
 
N, A, B = [int(x) for x in input().split()]
X = [int(x) for x in input().split()]

ans = 0

for i in range(N - 1):
    if (X[i + 1] - X[i]) * A > B:
        ans += B
    else:
        ans += (X[i + 1] - X[i]) * A

print(ans)