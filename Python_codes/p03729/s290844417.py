a,b,c=input().split()
A=a[len(a)-1]
B=b[0]
B1=b[len(b)-1]
C=c[0]

if A==B and B1==C:
    print("YES")
else:
    print("NO")