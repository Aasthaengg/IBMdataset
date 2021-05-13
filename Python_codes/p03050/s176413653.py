n=int(input())
p=0
for i in range(1,int(n**0.5)+2):
    j,k=divmod(n-i,i)
    p+=0 if k or j<=i else j
print(p)