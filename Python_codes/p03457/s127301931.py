n = int(input())

list = [list(map(int, input().split())) for x in range(n)]

t = 0
x = 0
y = 0
flag = 0

for i in range(n):
    if i>0:
        t = list[i][0] - list[i-1][0]
        d = abs(list[i][1] - list[i-1][1] + list[i][2] - list[i-1][2])
    else:
        t = list[i][0]
        d = abs(list[i][1] + list[i][2])
    if (t-d) >= 0 and (d-t)%2 == 0:
        continue
    else:
        flag = 1
        print('No')
        break
if flag ==0:
    print('Yes')
