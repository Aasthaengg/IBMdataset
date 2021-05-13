n=int(input())

print(n*(n-1)//2-n//2)
for i in range(1,n):
    for q in range(i+1,n+1):
        if i+q!=n+1-n%2:
            print(i,q)