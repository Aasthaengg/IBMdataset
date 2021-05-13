x, y = map(int, input().split())
flag = 0
for i in range(x+1):
    if 2*i + 4*(x-i) == y:
        flag = 1
        print('Yes')
        break
    else:
        continue
if flag == 0:
    print('No')