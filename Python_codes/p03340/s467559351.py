from itertools import groupby

N = int(input())
A = list(map(int, input().split()))

c = 0
add = 0
xor = 0
r = 0
for l in range(N):
    # print(l, r, bin(add)[2:], bin(xor)[2:])
    if r < l:
        r = l
        add = 0
        xor = 0
    while r < N and add+A[r] == xor^A[r]:
        add += A[r]
        xor ^= A[r]
        r += 1
        # print(l, r, add, xor)
    # l <= i < r までの add と xor が等しい
    c += r - l
    add -= A[l]
    xor ^= A[l]
    # print(add, xor, c)

print(c)