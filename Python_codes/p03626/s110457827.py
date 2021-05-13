from itertools import groupby
n = int(input())
list_S = input()
list_E = input()
list_MAP = []
list_C = groupby(list_S)
for num, gr in list_C:
    list_MAP.append(len(list(gr)))
ans = 1
if list_MAP[0] == 2:
    ans *= 6
else:
    ans *= 3

for i in range(1, len(list_MAP)):
    if list_MAP[i-1] == 1 and list_MAP[i] == 1:
        ans *= 2


    if list_MAP[i-1] == 1 and list_MAP[i] == 2:
        ans *= 2


    if list_MAP[i-1] == 2 and list_MAP[i] == 1:
        ans *= 1


    if list_MAP[i-1] == 2 and list_MAP[i] == 2:
        ans *=3



ans = ans % 1000000007
print(ans)