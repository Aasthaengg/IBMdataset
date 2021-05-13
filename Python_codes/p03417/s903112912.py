N, M = map(int, input().split())
# print(NM)
if N == 1 and M == 1:
    print(1)
elif N == 1 and M > 1:
    print(M-2)
elif M == 1 and N > 1:
    print(N-2)
elif N >= 2 or M >= 2:
    print((N-2)*(M-2))
