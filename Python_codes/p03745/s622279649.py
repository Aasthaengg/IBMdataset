N = int(input())
A = list(map(int, input().split()))
B = []
i = 0
while i < N - 1:
    if A[i] != A[i+1]:
        B.append(A[i])
    i += 1
B.append(A[-1])

ans = 1
i = 0
while i < len(B) - 2:
    if (B[i + 1] - B[i]) * (B[i + 2] - B[i + 1]) < 0:
        ans += 1
        i += 2
    else:
        i += 1
print(ans)
