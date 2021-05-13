k, t = map(int,input().split())
a_l_init = list(map(int,input().split()))

if t == 1:
    print(k-1)
    exit()

a_l = []
for i, a in enumerate(a_l_init):
    a_l.append([a,i])
a_l.sort(reverse=True)

flag = 0
yesterday = -1
for _ in range(k):
    for j in range(t):
        if a_l[j][1] != yesterday:
            a_l[j][0] -= 1
            yesterday = a_l[j][1]
            a_l.sort(reverse=True)
            break
        elif a_l[j+1][0] != 0:
            continue
        else:
            flag = 1
            break
    if flag == 1:
        break

if flag == 0:
    print(0)
else:
    print(a_l[0][0])