n = int(input())
low = 0
hi = 10**9

li = []
lin = []

for _ in range(n):
    x,y,h = map(int,input().split())
    if h != 0:
        li.append((x,y,h))
    lin.append((x,y,h))

for i in range(101):
    for j in range(101):
        flag = True
        h = li[0][2]+abs(i-li[0][0])+abs(j-li[0][1])
        for a,b,c in lin:
            if max(h-abs(i-a)-abs(j-b),0) != c:
                flag = False
                break
        if flag:
            print(i,j,h)
            exit()