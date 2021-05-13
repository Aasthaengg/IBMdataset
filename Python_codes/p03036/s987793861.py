a,b,c= input().split()
x,y,z=(int(a),int(b),int(c))
ds = z
for i in range(10):
    ds_1 = ds 
    ds =x * ds - y 
    print(ds)