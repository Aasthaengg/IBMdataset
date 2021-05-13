a, b, c, d = map(int, input().split())
lw = a + b
rw = c + d
if lw > rw :
    print("Left")
elif lw == rw :
    print("Balanced")
elif lw < rw :
    print("Right")