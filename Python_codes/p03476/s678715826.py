def ERTS(N):
    table = [True]*(N+1)
    table[0], table[1] = False, False
    n = 2
    while n < N**0.5+1:
        if n:
            for i in range(n*2, N+1, n):
                table[i] = False
        n += 1
    return table

table = ERTS(10**5)
prime = []
for i in range(10**5+1):
    if table[i]:
        prime.append(i)

lst = []       
for p in prime:
    if table[(p+1)//2]:
        lst.append(p)

import bisect
Q = int(input())
for _ in range(Q):
    L, R = map(int, input().split())
    l = bisect.bisect_left(lst, L)
    r = bisect.bisect(lst, R)
    print(r - l)    