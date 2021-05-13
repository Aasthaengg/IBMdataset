a,b,n = list(map(int, input().split()))
t = 0
n = min(b-1,n)

print((a*n)//b - a*(n//b))