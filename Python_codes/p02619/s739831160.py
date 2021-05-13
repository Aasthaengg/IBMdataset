d = int(input())
ci = list(map(int, input().split()))
sdi_list = []
for i in range(d):
    sdi = list(map(int, input().split()))
    sdi_list.append(sdi)
td_list = []
for i in range(d):
    td = int(input())
    td_list.append(td)
lastdi = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
manzoku = 0
for i in range(d):
    manzokuteika = 0
    lastdi[td_list[i]-1] = i + 1
    for j in range(26):
        manzokuteika = manzokuteika + ci[j] * (i + 1 - lastdi[j])
    manzoku = manzoku + sdi_list[i][td_list[i]-1] - manzokuteika
    print(manzoku)
