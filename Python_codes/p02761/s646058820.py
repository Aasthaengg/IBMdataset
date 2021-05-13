N,M = map(int,input().split())
SC = [tuple(map(int,input().split())) for i in range(M)]

for n in range(1000):
    if len(str(n)) != N: continue
    for s,c in SC:
        if str(n)[s-1] != str(c):
            break
    else:
        print(n)
        exit()
print(-1)