N = int(input())
A = list(map(int, input().split()))

r = 0
res = 0
x = 0
s = 0
for l in range(N):
    while r < N and x ^ A[r] == s + A[r]:
        x ^= A[r]
        s += A[r]
        r += 1
    res += r - l

    if r == l:
        r += 1
    else:
        x ^= A[l]
        s -= A[l]

print(res)