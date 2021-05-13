l,r = map(int, input().split())

t = []

if r-l >= 2019:
    print(0)
else:
    for i in range(l,r):
        for j in range(l+1,r+1):
            t.append((i*j)%2019)
    print(min(t))