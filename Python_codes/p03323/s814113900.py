# input
A, B = map(int, input().split())

if abs(A - B) <= min(A, B):
    print("Yay!")
else:
    print(":(")