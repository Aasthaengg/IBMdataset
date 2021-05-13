n,x = map(int,input().split(" "))
l = list(map(int,input().split(" ")))
y = 0
for i in l:
    y += i
if y <= x:
    print(n+1)
else:
    count = 1
    d = 0
    j = 0
    while d < x:
        d += l[j]
        j += 1
        if d <= x:
            count += 1
    print(count)