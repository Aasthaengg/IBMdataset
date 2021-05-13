n,a,b = map(int,input().split())
mi = b + (n-1)*a
ma = a + (n-1)*b
if ma-mi+1 < 0:
    print(0)
else:
    print(ma-mi+1)