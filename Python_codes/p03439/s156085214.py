N = int(input())

def f(n):
    print(n, flush = True)
    S = input()
    if S == 'Vacant':
        exit()
    return S

l = 0
r = N
S = f(l)
for i in range(20):
    mid = (l + r) // 2
    U = f(mid)
    len = mid - l + 1
    if (len % 2 == 0 and S != U) or (len % 2 and S == U):
        l = mid
        S = U
    else:
        r = mid
