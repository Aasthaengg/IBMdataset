D,N = map(int,input().split())

if D == 0:
    c = N//100
    print(N+c)
else:
    tmp = 100 ** D
    c = N//100
    print(tmp*N+c*tmp)