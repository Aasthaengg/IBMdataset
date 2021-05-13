n=int(input())
m=n-1

p=int(m**(1/2))
c=0

for i in range(1,p+1):
        c+=(m//i-(i-1))*2-1
        
print(c)