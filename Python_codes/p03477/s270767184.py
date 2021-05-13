a,b,c,d=[int(i) for i in input().split()]

left=a+b
right=c+d

if left>right:
    print("Left")
elif left<right:
    print("Right")
else:
    print("Balanced")