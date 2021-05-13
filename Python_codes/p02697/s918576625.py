n,m=map(int,input().split())
l=m//2
for i in range(l):
    print(1+i,1+2*l-i)
for j in range(m-l):
    print(1+2*l+1+j,2*m+1-j)