from sys import stdin 
n,m,d = map(int,stdin.readline().split())
ans =  (1.0 * (n-d)*(m-1))/(n*n)
if d:
    ans*= 2 
print ans 