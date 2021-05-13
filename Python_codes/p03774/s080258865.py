import numpy as np

N, M = map(int, input().split())
ab = [list(map(int, input().split())) for i in range(N)]
cd = [list(map(int, input().split())) for i in range(M)]

for i in range(N):
    person = np.asarray(ab[i])
    shortest = 10**18
    for j in range(M):
        point = np.asarray(cd[j])
        diflist = person - point
        dif = abs(diflist[0])+abs(diflist[1])
        if dif < shortest:
            shortest = dif
            count = j+1
    print(count)
