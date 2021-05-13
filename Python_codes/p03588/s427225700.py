import sys
input = sys.stdin.readline
N = int(input())
ab = [tuple(map(int, input().split())) for _ in range(N)]
ab.sort()
ans = ab[-1][0] - ab[0][0] + 1
ans += ab[0][0] - 1
ans += ab[-1][1]

print(ans)
