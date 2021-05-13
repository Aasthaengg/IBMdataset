n = int(input())
a = list(map(int,input().split()))
t = abs(a[0])
dis = []
for i in range(1,n):

    t += abs(a[i] - a[i-1])


t += abs(a[-1])


before = 0
for i,now in enumerate(a):

    if i == n-1:
        after = 0
    else:
        after = a[i+1]


    if before <= now <= after or after <= now <= before:
        dis.append(0)
    elif before <= after <= now or now <= after <= before:
        dis.append(2 * abs(now - after))
    else:
        dis.append(2 * abs(now - before))
    before = now

for i, d in enumerate(dis):
    print(t-d)
