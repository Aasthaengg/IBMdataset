k,n=int(input()),50
b,c=k%n,k//n
d=n-b
print(n)
print(*[n+c]*b+[d+c-1]*d)