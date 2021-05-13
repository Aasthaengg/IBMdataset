a = list(map(int,input().split()))
x = a[0] + a[1]
y = a[2] + a[3]
if x > y:
    print("Left")
elif x == y:
    print("Balanced")
else :
    print("Right")