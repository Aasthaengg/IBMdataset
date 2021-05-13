n = int(input())
lis = [list(map(int, input().split())) for _ in range(n)]

lis.sort(key=lambda x:x[1])

flag = 1
total = 0

for i in lis:
    total += i[0]
    if total > i[1]:
        flag = 0
        break

if flag:
    print('Yes')
else:
    print('No')
