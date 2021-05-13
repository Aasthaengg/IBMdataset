N,D=map(int,input().split())
a=N//(2*D+1)
if N%(2*D+1)==0:
    print(a)   
else:
    print(a+1)