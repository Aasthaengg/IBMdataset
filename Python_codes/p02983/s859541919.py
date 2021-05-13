L, R = map(int, input().split())
if R-L+1>=2019:
    print(0)
else:
    a=2018
    for i in range(L, R+1):
        for j in range(i+1, R+1):
            a=min(a, ((i%2019)*(j%2019)%2019))
    print(a)