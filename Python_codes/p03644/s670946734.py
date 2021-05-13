N = int(input())
if N==1:
    print(1)
else:
    k = 1
    while 2**k<=N:
        k += 1
    print(2**(k-1))