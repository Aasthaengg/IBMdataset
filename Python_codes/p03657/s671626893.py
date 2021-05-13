A, B = map(int, input().split())

a = A % 3
b = B % 3
ab = (A + B) % 3

if (a == 0) or (b == 0) or (ab == 0):
    print("Possible")

else:
    print("Impossible")