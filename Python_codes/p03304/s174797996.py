n,m,d = map(int, input().split())
s = (2-(d==0))*(m-1)*(n-d)
t = n**2
print(s/t)