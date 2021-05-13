a,b=[int(x) for x in input().split(" ")]
x=(b-2*a)/2
y=(4*a-b)/2
print("Yes" if x>=0 and y>=0 and x%1==0.0 and y%1==0.0 else "No")
