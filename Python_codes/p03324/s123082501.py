a,b = map(int,input().split())
if b == 100:
    print((100**a)*101)
    exit()
print((100**a)*b)