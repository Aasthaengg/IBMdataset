n = int(input())
x,y = 0,0
for i in range(n):
    d = input().split()
    if d[0] == d[1]:
        x += 1
        y += 1
    else:
        a = list(d[0])
        b = list(d[1])
        for i in range(min(len(a),len(b))):
            if int(a[i],36) > int(b[i],36):
                x += 3
                break
            elif int(a[i],36) < int(b[i],36):
                y += 3
                break
            if i == min(len(a),len(b))-1:
                if len(a) < len(b):
                    y += 3
                else:
                    x += 3

print(x,y)