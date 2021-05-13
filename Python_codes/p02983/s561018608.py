L,R = map(int,input().split())
m = 10**18
if R-L>=2019:
    print(0)
else:
    for i in range(L,R):
        for j in range(i+1,R+1):
            m = min(m,i*j%2019)
    print(m)