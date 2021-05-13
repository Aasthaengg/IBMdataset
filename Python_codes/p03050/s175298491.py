n=int(input())

#n=m*a+a
#n=(m+1)*a
#m>a

if n==1 or n==2:
    print(0)
    exit()

cnt=0
for i in range(1,int(n**(0.5))+1):
    if n%i==0:
        m=n//i-1
        if n%m==n//m:
            cnt+=m
print(cnt)
        
    
