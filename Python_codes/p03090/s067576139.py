n=int(input())
m=(n*(n-1)//2)-(n//2)
print(m)
x=n+1-n%2
for i in range(1,n):
    for j in range(i+1,n+1):
        if i+j!=x:
            print(i,j)
    


