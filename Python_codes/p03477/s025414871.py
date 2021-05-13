ABCD = [int(i) for i in input().split()]
if ABCD[0] + ABCD[1] > ABCD[2] + ABCD[3]:
    print("Left")
elif ABCD[0] + ABCD[1] < ABCD[2] + ABCD[3]:
    print("Right")
else:
    print("Balanced")
