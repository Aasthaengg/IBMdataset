A,B,C=map(int,input().split())
if A+B<C:
    print(0,0)
elif A>C:
    print(A-C,B)
else:
    print(0,B-C+A)