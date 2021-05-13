n,x = map(int,input().split())
m = []
count = 0
for i in range(n):
    m.append(int(input()))

if (x-sum(m)) < min(m):
    print(n)
else:
    res = x - sum(m)
    while True:
        count = count+1
        res = res - min(m)
        if res < min(m):
            print(count+n)
            break
