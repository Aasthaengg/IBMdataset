n = int(input())

flag = 0
for i in range(n):
    d1, d2 = map(int, input().split())
    if d1==d2:
        flag += 1
    else:
        flag = 0
    if flag==3:
        break

if flag==3:
    print('Yes')
else:
    print('No')