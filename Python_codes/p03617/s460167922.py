q, h, s, d = (int(i) for i in input().split())
n = int(input())
x = min(4*q, 2*h, s)
y = min(2*x, d)
print( (y*(n-n%2)//2) + x*(n%2) )