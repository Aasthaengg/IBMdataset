import math
N, K = list(map(int, input().split()))
A = list(map(int, input().split()))

l, r = (A[0], 1)
def is_ok(c):
    x = sum([math.ceil(a/c)-1 for a in A])
    return x <= K

l, r = max(A), 0
while l - r > 1:
    c = (l + r) // 2
    if is_ok(c):
        l = c
    else:
        r = c
print(l)
