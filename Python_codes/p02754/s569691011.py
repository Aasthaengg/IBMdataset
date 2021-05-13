N, A, B = map(int, input().split())
ans = N // (A+B)
res = (N % (A+B))
if res > A:
    res = A
else:
    pass
print((ans*A)+res)