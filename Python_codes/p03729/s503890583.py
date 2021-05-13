x,y,z=input().split()
lx=len(x)
ly=len(y)
lz=len(z)
if x[lx-1]==y[0]:
    if y[ly-1]==z[0]:
        print("YES")
    else:
        print("NO")
else:
    print("NO")