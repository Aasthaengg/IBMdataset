a,b,c,d=[int(c) for c in input().split()]
X=sorted([a,b,c])
print("Yes" if (X[2]-X[1]<=d and X[1]-X[0]<=d) or abs(a-c)<=d else "No")