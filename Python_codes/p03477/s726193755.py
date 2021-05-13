l = list(map(int,input().split()))
if l[0]+l[1] > l[2]+l[3]:
    print("Left")
elif l[0]+l[1] < l[2]+l[3]:
    print("Right")
else:
    print("Balanced")
