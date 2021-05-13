import itertools

n, a, b, c = list(map(int, input().split()))

f = [a, b, c]
l = [int(input()) for _ in range(n)]

x = [0, 1, 2, 3]

mp_min = 10000

for sublist in itertools.product(x, repeat = n):
    flag = True
    mp = 0
    length = [0] * 3
    for j in range(n):
        d = sublist[j]
        if  d != 3:
            if length[d] == 0:
                length[d] = l[j]
            else:
                length[d] += l[j]
                mp += 10
    
    for k in range(3):
        if length[k] == 0:
            flag = False
            break
        else:
            mp += abs(length[k] - f[k])

    if flag:
        mp_min = min(mp_min, mp)

print(mp_min)