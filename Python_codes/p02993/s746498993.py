import sys
a=sys.stdin.readline()
b=list(a)
A,B,C,D = [int(b[i]) for i in (0,1,2,3)]
if A==B or B==C or C==D:
    print("Bad")
else:
    print("Good")