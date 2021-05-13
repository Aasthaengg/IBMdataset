N = int(input())

con = True
for h in range(1,3500):
    for n in range(h,3500):
        memo1 = N*h*n
        memo2 = 4*h*n-N*n-N*h
        if memo2 != 0:
            memo3 = memo1/memo2
            memo4 = memo1%memo2
            if (memo4==0) and (memo3>=1):
                print(h,n,int(memo3))
                con = False
                break
    if not(con):
        break
