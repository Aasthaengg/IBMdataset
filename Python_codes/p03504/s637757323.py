n, channel = map(int, input().split())
STC = []
for _ in range(n):
    s, t, c = map(int, input().split())
    STC.append([2*s,2*t,c])

STC = sorted(STC, key=lambda x: (x[2], x[1]))
# print(STC)

now_s = STC[0][0]
now_t = STC[0][1]
now_c = STC[0][2]

All_bangumi = []

for i in range(1,n):
    if now_c == STC[i][2]:
        if now_t == STC[i][0]:
            now_t = STC[i][1]
            if i == n-1:
                All_bangumi.append([now_s, now_t])
        else:
            All_bangumi.append([now_s, now_t])
            now_s = STC[i][0]
            now_t = STC[i][1]

    else:   
        All_bangumi.append([now_s, now_t])
        now_s = STC[i][0]
        now_t = STC[i][1]
        now_c = STC[i][2]
        if i == n-1:
            All_bangumi.append([now_s, now_t])

if n == 1:
    All_bangumi.append([STC[0][0], STC[0][1]])

for i in range(len(All_bangumi)):
    All_bangumi[i][0] = All_bangumi[i][0] -1


Imos = [0 for _ in range(2*(10**5)+1)]
for i in range(len(All_bangumi)):
    Imos[All_bangumi[i][0]] += 1
    Imos[All_bangumi[i][1]] -= 1

Imos_rui = [0]
for i in range(len(Imos)):
    Imos_rui.append(Imos_rui[-1]+Imos[i])

print(max(Imos_rui))