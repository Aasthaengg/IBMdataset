a, b, c = map(int, input().split())
a1, a2 = a//2, (a+1)//2
x = b*c*(a2-a1)
b1, b2 = b//2, (b+1)//2
y = a*c*(b2-b1)
c1, c2 = c//2, (c+1)//2
z = a*b*(c2-c1)
print(min(x, y, z))
