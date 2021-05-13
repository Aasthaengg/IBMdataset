n,m,d = [int(i) for i in input().split()]
x = 2
if d == 0 :x=1
print((n-d)*x*(m-1)/(n*n))