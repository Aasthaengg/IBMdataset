n,*A=map(int,open(0).read().split());m=1000
for x,y in zip(A,A[1:]):m+=m//x*(y-x)*(x<y)
print(m)