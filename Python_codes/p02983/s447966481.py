l,r = map(int,input().split())
dl = l % 2019
dr = r % 2019
lis = []
if r - l >= 2019 - dl or dl == 0:
    print(0)
else:
    for i in range(dl,dr):
        for j in range(i+1,dr+1):
            lis.append((i*j)%2019)
    print(min(lis))
