w, h, n = map(int,input().split())
ls = [[int(i) for i in input().split()] for j in range(n)]

x = list(range(0,w+1))
y = list(range(0,h+1))

for l in ls:
    if len(x)<=1 or len(y)<=1:
        break

    if l[2] == 2:
        x = [i for i in x if i <= l[0]]
    elif l[2] == 1:
        x = [i for i in x if i >= l[0]]
    elif l[2] == 4:
        y = [i for i in y if i <= l[1]]
    elif l[2] == 3:
        y = [i for i in y if i >= l[1]]

if len(x)<=1 or len(y)<=1:
    print(0)
else:
    x = max(x) - min(x)
    y = max(y) - min(y)
    print(x*y)
