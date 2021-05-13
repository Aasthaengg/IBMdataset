n = int(input())
list_s = [input() for x in range(0, n)]
list_count = [0, 0, 0, 0]

for si in list_s:
    if si == 'AC': list_count[0] += 1
    elif si == 'WA': list_count[1] += 1
    elif si == 'TLE': list_count[2] += 1
    else: list_count[3] += 1

print('AC x ' + str(list_count[0]))
print('WA x ' + str(list_count[1]))
print('TLE x ' + str(list_count[2]))
print('RE x ' + str(list_count[3]))