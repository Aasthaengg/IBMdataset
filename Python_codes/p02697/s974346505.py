N, M = map(int, input().split())
if N%2==0:
    for i in range(M):
        x = 0
        if i>=M/2:
            x = 1
        a = 1 + i
        b = N - i
        print(a+x, b)
else:
    n = (N//2)*2
    for i in range(M):
        a = 1 + i
        b = a + n - (2*i+1)
        print(a, b)