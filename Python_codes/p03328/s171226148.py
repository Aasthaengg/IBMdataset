icase=0
if icase==0:
    import sys
    a,b=map(int,input().split())
    for i in range(1,999):
        isum=(i*(i+1))//2-a
        for j in range(i,1000):
            jsum=(j*(j+1))//2-b
            if jsum==isum and 1<=jsum and j==i+1:
                print(jsum)
                sys.exit()
