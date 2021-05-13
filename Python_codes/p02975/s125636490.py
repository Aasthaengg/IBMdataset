N = int(input())
a = list(map(int, input().split()))
d = {}
for i in a:
    if i not in d:
        d[i] = 1
    else:
        d[i] +=1
if len(d) == 1 and 0 in d:
    print('Yes')
elif len(d) == 2:
    for i in d:
        if i == 0 and d[i] * 3 != N or i != 0 and d[i] * 3 != 2 * N:
            print('No')
            exit()
    print('Yes')
elif len(d) == 3:
    s = 0
    for i in d:
        s ^= i
        if d[i] * 3 != N:
            print('No')
            exit()
    if s != 0:
        print('No')
    else:
        print('Yes')
else:
    print('No')
