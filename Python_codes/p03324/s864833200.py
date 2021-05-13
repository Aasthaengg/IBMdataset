D, N = map(int, input().split())
if D == 0:
    print(N if N != 100 else 101)
elif D == 1:
    print(N*100 if N != 100 else 101 * 100)
elif D == 2:
    print(N*10000 if N != 100 else 101 * 10000)