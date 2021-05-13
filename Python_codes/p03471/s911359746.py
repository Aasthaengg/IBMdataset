n, y = list(map(int, input().strip().split()))
f=0
a=-1
b=-1
c=-1
for i  in range(0,n+1):
    for j in range(0,n-i+1):
        x=i*10000+j*5000+(n-i-j)*1000
        if y==x:
           a=i
           b=j
           c=n-i-j
print(a,b,c)