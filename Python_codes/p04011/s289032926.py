n, k = int(input()), int(input())
x,y = int(input()), int(input())
if n>k: 
    a = n-k
    print((x*k) + (y*a))
else: 
    print(x*n)

