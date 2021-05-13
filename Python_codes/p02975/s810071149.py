N = int(input())
A = list(map(int, input().split()))


As = set(A)

if len(As) == 3:
    k = 0
    x, y, z = As
    if x^y != z and x^z != y and y^z != x:
        print('No')
        k = 1
    n = N // 3
    if k == 0:
        for i in [x, y, z]:
            if A.count(i) != n and A.count(i) != n+1:
                k = 1
                print('No')
                break
        if k == 0:
            print('Yes')
elif len(As) == 2:
    k = 0
    if 0 in As:
        if A.count(0) == 2:
            pass
        elif A.count(0) == N//3 or A.count(0) == N//3 + 1:
            k = 1
            print('Yes')
    if k == 0:
        print('No')
elif len(As) == 1:
    if 0 in As:
        print('Yes')
    else:
        print('No')
else:
    print('No')
