import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 9)
MOD = 10 ** 9 + 7

N = int(input())

A_ = list(map(int, input().split()))

A = [A_[i] - i - 1 for i in range(N)]
A.sort()

tmp = A[N // 2]

ans = 0
for a in A:
    ans += abs(tmp - a)

print (ans)