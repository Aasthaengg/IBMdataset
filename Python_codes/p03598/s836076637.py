N = int(input())
K = int(input())
x = list(map(int, input().split()))
A = [0] * N
B = [0] * N

ans = 0
for i in range(N):
    x[i] = [x[i], i+1]
    A[i] = [0, i+1]
    B[i] = [K, i+1]

    if x[i][1] == A[i][1] == B[i][1]:
        ans += min(abs(x[i][0] - A[i][0]), abs(x[i][0] - B[i][0]))

print(ans*2)