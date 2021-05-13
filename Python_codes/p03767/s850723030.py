import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
A.sort()

ans = 0
for i in range(N, 3 * N, 2):
    ans += A[i]

print(ans)
