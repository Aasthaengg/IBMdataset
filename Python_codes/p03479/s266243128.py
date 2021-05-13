x,y=map(int,input().split())
tmp=x
for i in range(y+1):
    tmp=x*2**i
    if tmp >y:
        print(i)
        break
