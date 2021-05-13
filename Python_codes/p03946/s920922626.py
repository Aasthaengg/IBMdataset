import sys
input = sys.stdin.readline

N, T = [int(x) for x in input().split()]
A = [int(x) for x in input().split()]

ans = [-1, 0] # [最大の差, 個数]
max_right = -1

for i in range(N - 2, -1, -1):
    if A[i + 1] > max_right:
        max_right = A[i + 1]
    left = A[i]
    if max_right - left > ans[0]:
        ans = [max_right - left, 1]
    elif max_right - left == ans[0]:
        ans[1] += 1

print(ans[1])
    


