import sys

mod = 10**9 + 7
input = sys.stdin.readline
N = int(input())
A = list(map(int, input().split()))

ans = 1
xyz = [0] * 3
for i in range(N):
    tmp = 0
    index = -1
    for j in range(3):
        if A[i] == xyz[j]:
            tmp += 1
            if index == -1:
                index = j

    xyz[index] += 1
    ans *= tmp
    ans %= mod

    # print(xyz)
    # print(ans)

print(ans)