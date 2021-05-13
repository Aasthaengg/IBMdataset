import math

N = int(input())
s = int(math.sqrt(2*N))
if s*(s+1) != 2*N:
    print('No')
else: 
    print('Yes')
    print(s+1)
    a = []
    for i in range(1, s+1):
        n0 = 1 + s*(i-1) - (i-2)*(i-2+1)//2
        a.append(n0)
    w = a[-1] + 1 ; a.extend((w, w))  #;print(a); print()

    for i in range(s+1):
        nL = []
        for k in range(i):
            nL.append(a[k]+(i-k-1))
            #print('i, k, a[k]+(i-k)', i, k, a[k]+(i-k-1))
        nL = nL + list(range(a[i], a[i+1]))
            #print('+', list(range(a[i], a[i+1])))  ;print()
        print(s, *nL)