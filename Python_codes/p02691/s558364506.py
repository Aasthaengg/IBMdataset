# coding: utf-8
N = int(input())
A = [int(x) for x in input().split()]

L = dict(); R = dict()
for i in range(N):
    L[i + A[i]] = L.get(i + A[i], 0) + 1
    R[i - A[i]] = R.get(i - A[i], 0) + 1

ans = 0
# i + A[i] >= 2, i - A[i] <= N
for i in range(N):
    ans += L.get(i, 0) * R.get(i, 0)

print(ans)