n,k = map(int, input().split())

al = list(map(int, input().split())) 

if n==k:
    print(1)
    exit()
    
x = 1+(n-k)//(k-1)
y = (n-k)%(k-1)

if y >0:
    print(x+1)
else:
    print(x)