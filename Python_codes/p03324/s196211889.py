d,n=map(int,input().split())
if (100**d)*100<=(100**d)*n:
    print(((100**d)*n)+100**d)
else:
    print(((100**d)*n))