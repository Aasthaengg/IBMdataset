N = int(input())
A = list(map(int, input().split()))

ans = 0
for i, a in enumerate(A):
    if A[a - 1] == i + 1:
        ans += 1
ans //= 2
print(ans)
