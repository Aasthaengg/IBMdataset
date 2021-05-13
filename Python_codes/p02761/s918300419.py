n, m = map(int,input().split())
lst = []
for _ in range(m):
    lst.append(list(map(int,input().split())))

number = [[] for _ in range(n)]
for v in lst:
    keta,num = v[0]-1,v[1]
    if number[keta] == []:
        number[keta] = num

    if number[keta] != num:
        print(-1)
        exit()

if n == 1:
    if not number[0]:
        print(0)
    else:
        print(''.join([str(i) for i in number]))
elif n == 2:
    if number[0] == 0:
        print(-1)
        exit()
    else:
        if not number[0]:
            number[0] = 1
        if not number[1]:
            number[1] = 0
        print(''.join([str(i) for i in number]))
else:
    if number[0] == 0:
        print(-1)
        exit()
    else:
        if not number[0]:
            number[0] = 1
        if not number[1]:
            number[1] = 0
        if not number[2]:
            number[2] = 0
        print(''.join([str(i) for i in number]))
