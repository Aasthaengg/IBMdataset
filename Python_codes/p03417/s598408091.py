N, M = map(int, input().split())

if N >= 3 and M >= 3:
    print((M-2)*(N-2))
elif N ==1 and M == 1:
    print(1)
elif N == 1 and M >= 3:
    print(M-2)
elif M ==1 and N >= 3:
    print(N-2)
else:
    print(0) 