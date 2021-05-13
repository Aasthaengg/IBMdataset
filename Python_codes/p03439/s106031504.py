n = int(input())

l = 0
r = n-1

print(l)
seet = input()
if seet == 'Vacant':
    exit(0)

for _ in range(19):
    q = (l+r)//2

    # 区間が2つの時
    # 0-1 1//2=0
    if l == q:
        print(l+1)
        exit(0)

    print(q)
    tmp = input()
    if ((q-l) & 1 == 0 and tmp == seet) or ((q-l) & 1 == 1 and tmp != seet):
        l = q
        seet = tmp
    else:
        r = q-1
