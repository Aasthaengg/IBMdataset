N = int(input())
A = list(map(int, input().split()))

ct = 0
s = 0
xor = 0
r = 0
for l in range(N):
    while r < N and s+A[r] == xor ^ A[r]:
        xor ^= A[r]
        s += A[r]
        r += 1
    # print(l,r)
    ct += r-l
    s -= A[l]
    xor ^= A[l]
    # print(s,xor)
print(ct)
