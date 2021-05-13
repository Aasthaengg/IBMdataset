N = int(input())
a = list(map(int, input().split()))
l = [0, 0, 0, 0, 0, 0, 0, 0]
pro = 0
m1 = 0
m2 = 0

for i in a:
    if i < 400:
        l[0] += 1
    elif 400 <= i and i < 800:
        l[1] += 1
    elif 800 <= i and i < 1200:
        l[2] += 1
    elif 1200 <= i and i < 1600:
        l[3] += 1
    elif 1600 <= i and i < 2000:
        l[4] += 1
    elif 2000 <= i and i < 2400:
        l[5] += 1
    elif 2400 <= i and i < 2800:
        l[6] += 1
    elif 2800 <= i and i < 3200:
        l[7] += 1
    elif 3200 <= i:
        pro += 1

if l != [0, 0, 0, 0, 0, 0, 0, 0]:
    for i in l:
        if i != 0:
            m1 += 1
    m2 = m1 + pro
else:
    m1 = 1
    m2 = pro


print(m1, m2)
