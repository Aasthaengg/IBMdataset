S=input()
A=int(S[0])
B=int(S[1])
C=int(S[2])
D=int(S[3])
if A+B+C+D==7:
    print(A,'+',B,'+',C,'+',D,'=7',sep='')
elif A-B+C+D==7:
    print(A,'-',B,'+',C,'+',D,'=7',sep='')
elif A-B-C+D==7:
    print(A,'-',B,'-',C,'+',D,'=7',sep='')
elif A-B-C-D==7:
    print(A,'-',B,'-',C,'-',D,'=7',sep='')
elif A+B-C-D==7:
    print(A,'+',B,'-',C,'-',D,'=7',sep='')
elif A+B+C-D==7:
    print(A,'+',B,'+',C,'-',D,'=7',sep='')
elif A-B+C-D==7:
    print(A,'-',B,'+',C,'-',D,'=7',sep='')
elif A+B-C+D==7:
    print(A,'+',B,'-',C,'+',D,'=7',sep='')