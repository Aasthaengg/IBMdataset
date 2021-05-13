# input
ABCD = list(map(int, input().split()))

# check
L = sum(ABCD[:2])
R = sum(ABCD[2:])
if L == R:
    print("Balanced")
elif L > R:
    print("Left")
else:
    print("Right")