a, b, c = map(int, input().split())
if a > b and a > c:
    print(b * c // 2)
elif b > a and b > c:
    print(a * c // 2)
else:
    print(a * b // 2)