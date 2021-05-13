import sys

input = sys.stdin.readline
N = int(input())
A = sorted(list(map(int, input().split())))
tmp = A[-1]
ans = 0
for i in A[:-1]:
    if abs(A[-1] // 2 - i) < tmp:
        tmp = abs(A[-1] // 2 - i)
        ans = i
    elif A[-1] % 2 != 0 and abs(A[-1] // 2 - i + 1) < tmp:
        tmp = abs(A[-1] // 2 - i + 1)
        ans = i
print(A[-1], ans)
