n = int(input())

tank = []
tank.append(['a'])
for i in range(n):
    tmp_tank = []
    for w in tank[i]:
        tmp_max = max(list(w))
        nxt_max = chr(ord(tmp_max)+1)
        for i in range(ord('a'), ord(nxt_max)+1):
            tmp_tank.append(w+chr(i))
    tank.append(tmp_tank)

for w in tank[n-1]:
    print(w)