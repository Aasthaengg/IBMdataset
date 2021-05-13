n,m = map(int, input().split())
l = [0] * n

ac = 0
wa = 0
ac_done = [False] * n

for _ in range(m):
    p, s = input().split()
    p = int(p)
    if ac_done[p-1]:
        continue
    else:
        if s == 'AC':
            ac += 1
            wa += l[p-1]
            ac_done[p-1] = True
        else:
            l[p-1] += 1 

print(ac,wa)