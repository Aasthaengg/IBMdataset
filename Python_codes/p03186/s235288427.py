A,B,C=map(int,input().split())

if A+B>C:
    print(B+C)
elif A+B==C:
    print(B+C)
elif A+B==C-1:
    print(B+C)
else:
    print(2*B+A+1)