N = int(input())
A = [int(_) for _ in input().split()]

ans = 0
for i in range(N):
    if A[A[i] - 1] == i + 1:
        ans += 1

print(ans // 2)
