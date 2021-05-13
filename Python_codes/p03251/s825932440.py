n,m,x,y=map(int,input().strip().split(" "))
ar1=[int(i) for i in input().strip().split(" ")]
ar2=[int(i) for i in input().strip().split(" ")]
ar1.append(x)
ar2.append(y)
m1=max(ar1)
m2=min(ar2)
if m2>m1:
    print("No War")
else:
    print("War")