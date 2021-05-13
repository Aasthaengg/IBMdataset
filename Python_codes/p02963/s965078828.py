s=int(input())
large=10**9
if s==10**18:
    print(0,0,10**9,1,0,10**9)
else:
    y3=s//large+1
    x3=y3*large-s
    print(0,0,10**9,1,x3,y3)
