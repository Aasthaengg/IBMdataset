#080_D
n, c = map(int, input().split())
stc = [list(map(int, input().split())) for _ in range(n)]
stc.sort(key= lambda x: (x[2], x[0]))
imo = [0 for _ in range(10 ** 5 + 2)]

for i in range(n):
    if i < n-1:
        if stc[i][2] == stc[i+1][2] and stc[i][1] == stc[i+1][0]:
            stc[i+1][0] = stc[i][0]
            continue
    
    s, t, c = stc[i]
    imo[s] += 1
    imo[t+1] -= 1

for i in range(10 ** 5 + 1):
    imo[i+1] += imo[i]

print(max(imo))