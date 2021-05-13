
def etrc(n1,n2,rs):
    for r in range(n1):
        rc[n2].append(rs+r)
        rc[n2+r+1].append(rs+r)

n=int(input())
#n=6
x=int(((1+8*n)**0.5-1)/2)

rc=[[] for i in range(x+2)]

if n!=x*(x+1)//2:
    print("No")
else:
    print("Yes")
    print(x+1)

    rs=1
    for i in range(x):
        n1=x-i
        n2=i
        etrc(n1,n2,rs)
        rs=rs+n1

    for i in range(x+1):
        print(x, end=" ")
        for j in range(x):
            print(rc[i][j], end=" ")
        print()
 