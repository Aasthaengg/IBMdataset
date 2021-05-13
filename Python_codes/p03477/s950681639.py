A, B, C, D = map(int, input().split())
AB = A + B
CD = C + D
if AB == CD:
    print("Balanced")
elif AB > CD:
    print("Left")
else:
    print("Right")