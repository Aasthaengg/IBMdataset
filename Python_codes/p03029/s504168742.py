import sys
a=sys.stdin.readline()
res = [int(i) for i in a.split() if i.isdigit()] 
A,P = [res[i] for i in (0,1)]
if type(A)==int and type(P)==int and (A>=0 and A<=100) and (P>=0 and P<=100):
    Pieces=P+(A*3)
    Pies=Pieces//2
    print(Pies)
else:
    print("Error")