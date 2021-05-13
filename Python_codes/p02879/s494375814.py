A,B=map(int,input().split())
check=[1,2,3,4,5,6,7,8,9]
if A in check and B in check:
    print(A*B)
else:
    print("-1")
