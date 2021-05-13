A, B, K = map(int, input().split())

AK = A-K

if AK < 0:
    BK = AK+B
    if BK < 0:
        print(0, 0)
    else:
        print(0, BK)
else:
    print(AK, B)
