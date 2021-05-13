l, r = map(int, input().split())
min = 10**5
if r-l >= 2018:
    print(0)
else:
    for i in range(l,r+1):
        for j in range(i+1, r+1):
            if i*j % 2019 < min:
                min = i*j % 2019
    print(min)


