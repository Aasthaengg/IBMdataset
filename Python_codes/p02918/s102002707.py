N, K = map(int, input().split())
S = input()
changeLR = []
changeRL = []
happy = 0
for i in range(N):
    if i == 0:
        before = S[0]
    else:
        tmp = S[i]
        if tmp == 'L' and before == 'R':
            changeLR.append(i)
        elif tmp == 'R' and before == 'L':
            changeRL.append(i)
        else:
            happy += 1
        before = tmp
koukan = min(len(changeLR), len(changeRL))
if K <= koukan:
    happy += 2 * K
elif K > koukan:
    if len(changeLR) != len(changeRL):
        happy += 2 * koukan + 1
    else:
        happy += 2 * koukan
print(happy)