A,B,C=map(int,input().split())

if max(A,B,C)*3%2==(A+B+C)%2:
    print((3*max(A,B,C)-(A+B+C))//2)
else:
    print((3*(max(A,B,C)+1)-(A+B+C))//2)