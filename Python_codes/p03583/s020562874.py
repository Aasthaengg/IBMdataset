N=int(input())
for h in range(3500,0,-1):
    for n in range(3500,0,-1):
        X=(4/N)-(1/h)-(1/n)
        if X>0 and X<=1:
            w=int(1/X)
            if 4/N==(1/h+1/n+1/w):
                print(h,n,w)
                exit()