N, M = list(map(int,input().rstrip().split()))
Amin = 1
Amax = N
for i in range(M):
    L, R = list(map(int,input().rstrip().split()))
    Amin = max(Amin,L)
    Amax = min(Amax,R)
    if Amin>Amax:
        print(0)
        break
else:
    print(Amax-Amin+1)