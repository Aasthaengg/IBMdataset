a,b,c,d = map(int,input().split())

left = a+b
right = c+d

if left < right:
    print("Right")
elif left == right:
    print("Balanced")
else:
    print("Left")