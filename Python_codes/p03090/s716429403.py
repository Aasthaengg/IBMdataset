n = int(input())
print(n*(n-1)//2-n//2)

m = n//2*2+1
for i in range(1,n):
    for j in range(i+1,n+1):
        if i+j!=m:
            print(i,j)