n,y=list(map(int, input().strip().split()))
a=-1
b=-1
c=-1
for i in range(n+1):
    for j in range(n-i+1):
        s=(y-10000*i-5000*j)
        if s==1000*(n-i-j):
            a=i
            b=j
            c=s//1000
            break
print(a,b,c)