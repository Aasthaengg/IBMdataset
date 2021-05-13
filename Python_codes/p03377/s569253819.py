def YN(P):
    if P:
        print("YES")
    else:
        print("NO")

a,b,x=map(int,input().split())
YN(a<=x<=a+b)