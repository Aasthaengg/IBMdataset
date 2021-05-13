a, b, c, d = list(map(int, input().split()))

y = a + b 
z = c + d 

if y==z:
    print("Balanced")
elif y>z:
    print("Left")
else:
    print("Right")