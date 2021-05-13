N, C = map(int, input().split())
stc = [list(map(lambda x:int(x), input().split())) for _ in range(N)]

stc = sorted(stc, key=lambda x:(x[2], x[0], x[1]))
l = []
i = N-1
s, t, c = 0, 0, 0
while i >= 0:
    if stc[i][2] == stc[i-1][2] and stc[i][0] == stc[i-1][1]:
        s = stc[i-1][0]
        if t == 0:
            t = stc[i][1]
        c = stc[i][2]
    else:
        if s != 0:
            l += [[s, t, c]]
            s, t, c = 0, 0, 0
        else:
            l += [stc[i]]

    i -= 1
        
imos = [0]*(2*10**5+1)
for s, t, c in l:
    imos[s-1] += 1
    imos[t] -= 1

for i in range(len(imos)-1):
    imos[i] = imos[i] + imos[i-1]

print(max(imos))



