L,R=map(int,input().split())
A=[]
if R-L>=2019:
    print(0)
else:
    d=2019
    for i in range(L,R):
        for j in range(i+1,R+1):
            d=min(i*j%2019,d)
    print(d)