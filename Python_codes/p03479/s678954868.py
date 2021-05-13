X, Y = map(int, input().split())
cn = 1
for i in range(10**7):
    X = X *2
    if X <= Y:
        cn = cn + 1
    else:
        print(cn)
        break