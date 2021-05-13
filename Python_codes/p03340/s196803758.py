inpl = lambda: list(map(int,input().split()))
N = int(input())
A = inpl()
ans = 0
xor = plus = A[0]
r = 1
for l in range(N):
    while r < N and xor^A[r] == plus+A[r]:
        xor ^= A[r]
        plus += A[r]
        r += 1
    ans += r-l
    xor ^= A[l]
    plus -= A[l]
print(ans)