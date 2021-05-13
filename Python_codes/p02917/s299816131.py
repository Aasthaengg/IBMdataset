N = int(input())
A = [0] * N
B = list(map(int, input().split()))
A[0] = B[0]
A[N - 1] = B[N - 2]
if N == 2:
    print(sum(A))
    quit()
for i in range(N - 2):
    if B[i + 1] >= B[i]:
        A[i + 1] = B[i]
    else:
        A[i + 1] = B[i + 1]
print(sum(A))