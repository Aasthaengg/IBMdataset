from collections import Counter
N = int(input())
A = list(map(int, input().split()))
cnt = Counter(A)
side = []
check = 4
A = sorted(set(A), reverse=True)
for i in A:
    if cnt[i] != 1:
        side.append(i)
        check -= cnt[i]
    if check <= 0:
        break
try:
    print(side[0]*side[1])
except IndexError:
    try:
        print(side[0]**2)
    except IndexError:
        print(0)
