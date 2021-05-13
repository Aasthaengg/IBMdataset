N = int(input())
A = list(map(int, input().split()))

a_cnt = {}
for ai in A:
    if ai in a_cnt:
        a_cnt[ai] += 1
    else:
        a_cnt[ai] = 1
from operator import itemgetter
a_cnt = sorted(a_cnt.items(), key=itemgetter(0), reverse=True)
tate = 0
yoko = 0
for i in range(len(a_cnt)):
    if a_cnt[i][1] >= 2:
        tate = a_cnt[i][0]
        #a_cnt[i][1] -= 1
        a_cnt[i] = (a_cnt[i][0], a_cnt[i][1] - 2)
        break
for i in range(len(a_cnt)):
    if a_cnt[i][1] >= 2:
        yoko = a_cnt[i][0]
        #a_cnt[i][1] -= 1
        a_cnt[i] = (a_cnt[i][0], a_cnt[i][1] - 2)
        break
#if tate == 0 or yoko == 0:
#    print(0)
print(tate * yoko)