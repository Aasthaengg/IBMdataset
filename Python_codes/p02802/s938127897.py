N, M = map(int, input().split())

ok = [False]*N
wa = [0]*N

for i in range(M):
    p, S = input().split()
    p = int(p) - 1
    if ok[p] == False:
        if S == "WA":
            wa[p] += 1
        else:
            ok[p] = True
    else:
        pass
pena = 0
for i in range(N):
    if ok[i] == True:
        pena += wa[i]
print(sum(ok), pena)