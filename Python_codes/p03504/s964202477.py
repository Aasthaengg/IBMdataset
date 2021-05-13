N, C = map(int, input().split())

STC = [tuple(map(int, input().split())) for i in range(N)]
STC.sort()

rec = []
for i in range(N):
    isFree = False
    for j in range(len(rec)):
        if (rec[j][0] < STC[i][0] and rec[j][1] != STC[i][2]) or (rec[j][0] <= STC[i][0] and rec[j][1] == STC[i][2]):
            isFree, rec[j] = True, (STC[i][1], STC[i][2])
            break
    if not isFree:
        rec.append((STC[i][1], STC[i][2]))

print(len(rec))
