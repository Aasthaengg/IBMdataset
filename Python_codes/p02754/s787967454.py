N,A,B=map(int,input().split())
c=N//(A+B)
d=N%(A+B)
print(c*A+min(d,A))