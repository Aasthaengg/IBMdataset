l,r = map(int, input().split())
min1 = 2019
for i in range(l, min(r+1, l+2020)):
    for j in range(i+1, min(r+1, l+2020)):
        candidate = ((i%2019)*(j%2019))%2019
        if candidate < min1:
            min1 = candidate
print (min1)