def factorial_(a):
    mem = 1
    for i in range(1, a+1):
        mem = (mem*i)%(10**9 + 7)
    return mem

N, M = map(int, input().split())
a = max([N, M])
b = min([N, M])

if abs(N - M) > 1:
    print(0)
else:
    print((factorial_(a) * (b-a+2) * factorial_(b))%(10**9 + 7))