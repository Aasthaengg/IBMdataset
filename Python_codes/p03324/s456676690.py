a,b=(int(i) for i in input().strip().split(" "))
if b!=100:
    print(b*(100**a))
else:
    print(101*(100**a))