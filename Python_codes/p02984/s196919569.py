N = int(input())
A = list(map(int, input().split()))
ans = []
S = sum(A)
S_2 = 0
for i in range(1, N - 1, 2):
    S_2 += A[i]
X1 = S - 2 * S_2
ans.append(str(X1))

for i in range(1, N):
    X = 2 * A[i - 1] - int(ans[i - 1])
    ans.append(str(X))
print(" ".join(ans))
