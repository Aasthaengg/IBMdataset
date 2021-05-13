from operator import itemgetter

n = int(input())
l = sorted([list(map(int, input().split())) for _ in range(n)], key=itemgetter(1))

count = 0
Work = True
for i in range(n):
    if count + l[i][0] > l[i][1]:
        Work = False
        break
    else:
        count += l[i][0]

if Work:
    print('Yes')
else:
    print('No')