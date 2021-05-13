import sys

sys.setrecursionlimit(10 ** 9)
input = sys.stdin.readline

H, W = [int(_) for _ in input().split()]
N = int(input())
A = [int(_) for _ in input().split()]
ai = 0
for i in range(H):
    ans = []
    for j in range(W):
        if A[ai] <= 0: ai += 1
        ans.append(ai + 1)
        A[ai]-=1
    if i %2==1:
        print(*reversed(ans))
    else:
        print(*ans)
