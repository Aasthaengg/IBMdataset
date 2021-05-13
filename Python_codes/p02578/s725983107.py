n = int(input())
A = list(map(int, input().split()))

ans = 0
max = A[0]

for i in range(1, n):
    if A[i] > max:
        max = A[i]
    else:
        ans += max - A[i]

print(ans)