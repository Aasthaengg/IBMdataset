a,b,c = map(int,input().split())
if (a*b*c)%2==0:
    print(0)
else:
    A=sorted([a,b,c])
    print(A[0]*A[1])