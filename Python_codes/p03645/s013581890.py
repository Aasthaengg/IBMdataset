n,m = map(int,input().split())

li1 = []
lin = []

for _ in range(m):
    a,b = map(int,input().split())
    if a == 1:
        li1.append(b)
    elif b == n:
        lin.append(a)

li1.sort()
lin.sort()

tmp = 0

if not len(lin):
    print('IMPOSSIBLE')
    exit()

for i in li1:
    while i > lin[tmp]:
        tmp += 1
        if tmp == len(lin):
            print('IMPOSSIBLE')
            exit()
    if i == lin[tmp]:
        print('POSSIBLE')
        exit()


print('IMPOSSIBLE')
