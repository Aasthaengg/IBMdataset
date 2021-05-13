n = int(input())
A = list(map(int, input().split()))

ans = 0
aa = A[0]
for i in range(1, n):
    if A[i] == aa:
        ans += 1
        A[i] = -1
    aa = A[i]
print(ans)
