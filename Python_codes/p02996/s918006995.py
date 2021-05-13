n = int(input())
l = [list(map(int,input().split())) for i in range(n)]
l.sort(key=lambda x: x[1])
now = 0
for i in range(n):
    now += l[i][0]
    if(now > l[i][1]):
        print('No')
        exit()
print('Yes')