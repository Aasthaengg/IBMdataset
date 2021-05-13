N = int(input())


LN = list(range(N+1))


SUM = 0


for i in LN:
    if ((LN[i] % 3 != 0) and (LN[i] % 5 != 0)):
        SUM = SUM + LN[i]

print(SUM)