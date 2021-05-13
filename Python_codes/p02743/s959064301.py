a, b, c = map(int, input().split())
if a + b >= c:
    print("No")
elif (c - a - b) ** 2 > 4 * (a * b):
    print("Yes")
else:
    print("No")