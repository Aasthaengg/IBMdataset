N, P = map(int, input().split())
A = list(map(int, input().split()))

resZero = resOne = 0
for a in A:
    if a % 2 == 0:
        resZero += 1
    else:
        resOne += 1

if resOne == 0:
    if P == 1:
        print(0)
    else:
        print(2 ** N)
else:
    print(2**(N-1))