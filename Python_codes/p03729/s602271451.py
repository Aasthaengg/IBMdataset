a, b, c = list(input().split())

d, e, f, g = a[-1], b[0], b[-1], c[0]

y = d == e 
z = f == g 

if (y == True) and (z==True):
    print("YES")
else:
    print("NO")