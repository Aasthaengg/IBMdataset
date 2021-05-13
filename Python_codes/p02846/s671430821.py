T1, T2 = map(int,input().split())
A1, A2 = map(int,input().split())
B1, B2 = map(int,input().split())

LA = T1*A1+T2*A2
LB = T1*B1+T2*B2
if LA == LB:
    print("infinity")
    exit()
elif LA < LB:
    LA, LB = LB, LA 
    A1, B1 = B1, A1
    A2, B2 = B2, A2

l = LA - LB
r = T1*B1-T1*A1 
if r < 0:
    print(0)
    exit()
else:
    # print("===")
    # print(l,r)
    if r%l==0:
        print( (r//l)*2)
    else:
        print( (r//l)*2 +1 )
