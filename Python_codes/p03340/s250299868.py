N, *A = map(int, open(0).read().split())

ans = 0
acc = 0
r = 0
for l in range(N):
    while r < N and (acc ^ A[r]) == acc + A[r]:
        acc += A[r]
        r += 1

    ans += r - l

    if l == r:
        r += 1
    else:
        acc -= A[l]

print(ans)