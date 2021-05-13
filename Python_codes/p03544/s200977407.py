N = int(input())
L1 = 2
L2 = 1
L3 = 3
if N == 0:
    print(L1)
elif N == 1:
    print(L2)
else:
    for i in range(N-2):
        L1 = L3
        L3 += L2
        L2 = L1
    print(L3)
