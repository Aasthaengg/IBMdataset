a,b,n = map(int, input().split())

s1 = (a*n)//b - a*(n//b)
x = max(1,n - n % b - 1)
s2 = (a*x)//b - a*(x//b) 

print(max(s1,s2))