N = int(input())
L0 = 2
L1 = 1
if N == 1:
    print(L1)
else:
    for i in range(N-1):
        L1, L0 = L1 + L0, L1
    print(L1)