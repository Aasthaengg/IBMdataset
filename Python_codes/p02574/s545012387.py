from math import gcd

N,*A = map(int, open(0).read().split())
m = max(A)
if m == 1:
    print('pairwise coprime')
else:
    minfactor = [-1] * (m+1)
    for i in range(2,m+1):
        if minfactor[i] == -1:
            for j in range(1,m//i+1):
                minfactor[i*j] = i
    temp = gcd(A[0],A[1])
    for i in range(2,N):
        temp = gcd(temp,A[i])
        if temp == 1:
            break
    if temp > 1:
        print('not coprime')
    else:
        s = set()
        for x in A:
            if x > 1:
                p = x
                while p > 1:
                    mf = minfactor[p]
                    if mf not in s:
                        s.add(mf)
                        while p % mf == 0:
                            p = p // mf
                    else:
                        break
                else:
                    continue
                print('setwise coprime')
                break
        else:
            print('pairwise coprime')