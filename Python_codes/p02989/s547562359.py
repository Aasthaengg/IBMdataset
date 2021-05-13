N = int(input())
D = list(map(int, input().split()))

D.sort()

if N % 2 == 1:
    print(0)
else:
    M = N //2
    res = D[M] - D[M-1]
    print(res)
