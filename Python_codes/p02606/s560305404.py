l,r,d=map(int,input().split())
x=(r-l)//d
if l%d!=0 and r%d!=0:
    print(x)
else:
    print(x+1)