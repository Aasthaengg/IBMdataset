N, M = map(int, input().split())
if N == 1 and M == 1:
    print(1)
elif (N == 1 and M >= 2) or (M == 1 and N > -2):
    print(max(N, M) - 2)
else:
    print((N - 2) * (M - 2))