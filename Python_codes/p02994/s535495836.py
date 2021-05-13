N,L=map(int,input().split())
a=[]
for i in range(1,N+1):
    a.append(L+i-1)
A=list(map(abs,a))
print(sum(a)-a[A.index(min(A))])