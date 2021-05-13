n, m = map(int, input().split())
Pref = [[0,0,0,''] for _ in range(m)]
for i in range(m):
    p,y = map(int,input().split())
    Pref[i] = [i,p,y,'']

Pref = sorted(Pref, key=lambda x: x[2])
Pref = sorted(Pref, key=lambda x: x[1])
c = 0
P = Pref[i][1]
for i in range(m):
    if P != Pref[i][1]:
        c = 1
        P = Pref[i][1]
    else:
        c += 1
    Pref[i][3] = str(Pref[i][1]).zfill(6) + str(c).zfill(6)

Pref = sorted(Pref, key=lambda x: x[0])
for i in range(m):
    print(Pref[i][3])