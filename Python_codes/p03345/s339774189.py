a, b, c, k = map(int, input().split())

if abs(a - b) >= 10e18:
    print("Unfair")
elif k%2 == 0:
    print(a - b)
else:
    print(b - a)