N, M = map(int, input().split())

if N <= 5:
    print(0)
elif 6 <= N <= 12:
    print(M // 2)
else:
    print(M)
