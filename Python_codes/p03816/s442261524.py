from collections import Counter

N =int(input())
cntA = Counter(map(int, input().split()))
len_cntA = len(cntA)
if len_cntA == 1:
    print(1)
    exit()

dif = 0
for key in cntA:
    dif += cntA[key] - 1

if dif % 2 == 1:
    print(len_cntA - 1)
else:
    print(len_cntA)
