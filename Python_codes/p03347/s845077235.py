def terminate():
    print(-1)
    exit()


N, *A = map(int, open(0).read().split())
if A[0] != 0:
    terminate()

ans = 0
for i in range(N - 1):
    if A[i + 1] - A[i] > 1:
        terminate()
    if A[i] + 1 == A[i + 1]:
        ans += 1
    else:
        ans += A[i + 1]
print(ans)
