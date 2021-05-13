A,B,C,D=map(int,input().split())
for i in range(1,1000):
    if i%2!=0:
        C-=B
        if C<=0:
            print('Yes')
            exit()
    else:
        A-=D
        if A<=0:
            print('No')
            exit()