a,b,c,d = map(int,input().split())
L = a+b
R = c+d
print("Left"*(L>R) or "Right"*(L<R) or "Balanced")