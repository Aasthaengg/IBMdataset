X, A, B = map(int, input().split())
BsubA = B - A

if BsubA <= 0:
    print("delicious")
elif X >= BsubA:
    print("safe")
else:
    print("dangerous")
