n = int(input())
P = [int(input())-1 for i in range(n)]

A = [0] * n
for i in range(n):
    A[P[i]] = i

ans = 1
ans1 = 1
for i in range(1, n):
    if A[i] > A[i-1]:
        ans1 += 1
    else:
        ans = max(ans1, ans)
        ans1 = 1
ans = max(ans1, ans)

print(n - ans)