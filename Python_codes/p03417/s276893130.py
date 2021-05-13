N, M = map(int, input().split())
if N==1 and M==1:
    print(1)
elif N<=2 and M<=2:
    print(0)
else:
    if N==1:
        M -= 2
    elif M==1:
        N -= 2
    else:
        M -= 2
        N -= 2
    print(N*M)