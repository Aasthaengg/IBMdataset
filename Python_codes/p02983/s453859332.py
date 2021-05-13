L,R = map(int,input().split())
if R-L+1>=673:
    print(0)
else:
    cmin = 2019
    for i in range(L,R):
        for j in range(i+1,R+1):
            cmin = min(cmin,(i*j)%2019)
    print(cmin)