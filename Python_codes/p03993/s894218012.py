N = int(input())
A = list(map(int, input().split()))
A = [a - 1 for a in A]

ans = 0
for i in range(N):
    if A[A[i]] == i:
        ans += 1
print(ans // 2)
