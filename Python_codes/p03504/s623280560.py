n, c = map(int, input().split())
L = [[0, 0, 0] for _ in range(n)]

rec = []

for i in range(n):
    s, t, c = map(int, input().split())
    c = c-1
    L[i][0] = s
    L[i][1] = t
    L[i][2] = c

L.sort(key=lambda x: x[0])

for i in range(n):
    s = L[i][0]
    t = L[i][1]
    c = L[i][2]
    if i == 0:
        rec.append([c, t])
    else:
        for j in range(len(rec)):
            if rec[j][0] == c and rec[j][1] <= s:
                rec[j][1] = t
                break
        else:
            rec.sort(key=lambda x: x[1])
            for k in range(len(rec)):
                if rec[k][1]+1 <= s:
                    rec[k][0] = c
                    rec[k][1] = t
                    break
            else:
                rec.append([c, t])
#print(rec)
print(len(rec))