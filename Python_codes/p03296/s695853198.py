n = int(input())
A = list(map(int, input().split()))

ans = 0
before = A[0]
for i in range(1, n):
    if A[i] == before:
        ans += 1
        before = 0
    else:
        before = A[i]
print(ans)
