N = int(input())
A = list(sorted(map(int, input().split())))

setA = set(A)

if A.count(0) == N:
    print('Yes')
elif len(setA) == 2 and A.count(0) == N / 3:
    print('Yes')
elif len(setA) == 3:
    setA = list(setA)
    x = setA[0]
    y = setA[1]
    z = setA[2]
    if x ^ y ^ z == 0 and A.count(x) == N / 3 and A.count(y) == N / 3:
        print('Yes')
    else:
        print('No')
else:
    print('No')
