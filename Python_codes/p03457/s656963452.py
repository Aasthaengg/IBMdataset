n = int(input())
lst = []
for _ in range(n):
    lst.append(list(map(int,input().split())))

now = [0,0]
time = 0

for i in range(n):
    t,x,y = lst[i][0], lst[i][1], lst[i][2]
    distance = abs(now[0]-x) + abs(now[1]-y)
    if (t - time) % 2 == 0 and distance % 2 == 0 and (t - time) >= distance:
        now = [x,y]
        time = t
    elif (t - time) % 2 != 0 and distance % 2 != 0 and (t - time) >= distance:
        now = [x,y]
        time = t
    else:
        print('No')
        exit()
print('Yes')