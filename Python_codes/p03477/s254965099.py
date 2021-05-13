A, B , C , D = map(int, input().split())
apple = A + B
dell = C + D
if dell > apple:
    print("Right")
elif dell < apple:
    print("Left")
else:
    print("Balanced")