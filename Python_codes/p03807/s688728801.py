n = int(input())
a = list(map(int,input().split()))

o,e = 0,0
for i in a:
    if i % 2 == 0:
        e += 1
    else:
        o += 1

if o % 2 == 1:
    print('NO')
    exit()

print('YES')