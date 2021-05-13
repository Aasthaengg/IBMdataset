N, K = map(int, input().split())

if(K%2 != 0):
    a = N//K
    print(a**3)
else:
    a = N//K
    if(N%K >= K//2):
        b = a+1
    else:
        b = a
    print(a**3+b**3)