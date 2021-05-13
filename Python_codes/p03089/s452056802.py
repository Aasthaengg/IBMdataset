n = int(input())
lst = list(map(int,input().split()))
stock = []
flg = True
for i in range(n):
    tmp = -100
    for j in range(len(lst)):
        if lst[j] == j+1:
            tmp = max(tmp, j)
    if tmp == -100:
        flg =  False
        break
    else:
        stock.append(lst[tmp])
        lst = lst[:tmp]+lst[tmp+1:]
if not flg:
    print(-1)
else:
    for x in stock[::-1]:
        print(x)