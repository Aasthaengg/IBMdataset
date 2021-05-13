from operator import itemgetter
n = int(input())
data = []
for _ in range(n):
    x,y,h = map(int,input().split())
    data.append((x,y,h))
data.sort(key=itemgetter(2),reverse=True)
for x in range(101):
    for y in range(101):
        c = -1
        for a,b,h in data:
            if c == -1:
                c = h+abs(a-x)+abs(b-y)
            else:
                if h != max(c-abs(a-x)-abs(y-b),0):
                    break
        else:
            print(x,y,c)
            exit()