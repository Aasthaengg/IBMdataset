ab = [list(map(int, input().split())) for _ in range(3)]
dict_ab = {}

for i in range(3):
    if ab[i][0] not in dict_ab:
        dict_ab[ab[i][0]] = 1
    else:
        dict_ab[ab[i][0]] += 1
    if ab[i][1] not in dict_ab:
        dict_ab[ab[i][1]] = 1
    else:
        dict_ab[ab[i][1]] += 1

if min(dict_ab.values()) == 1 and max(dict_ab.values()) == 2:
    print('YES')
else:
    print('NO')