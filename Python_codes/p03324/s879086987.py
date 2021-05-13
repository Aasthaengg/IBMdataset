D,N = map(int,input().split())
if D == 0:
    if N != 100:
        print(N)
    else:
        print(101)
    exit()
if D == 1:
    if N != 100:
        print(N*100)
    else:
        print(10100)
    exit()
if N != 100:
    print(N*10000)
else:
    print(1010000)