A, B, C, D = map(int, input().split())

L = int(A + B)
R = int(C + D)

if (L > R):
    print("Left")

elif(L == R):
    print("Balanced")

elif(L < R):
    print("Right")