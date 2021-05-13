l,r=map(int, input().split())
if(r-l>=2019):
    print(0)

else:
    l%=2019
    r%=2019
    res = 10000000000

    for i in range(min(l,r),max(l,r)):
        for j in range(i+1, max(l,r)+1):
            res = min(res,(i*j)%2019)
    print(res)
