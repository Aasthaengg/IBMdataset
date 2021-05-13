a, b, c, d = map(int, input().split())

if c > a and c-a <= d:
    print("Yes")

elif a > c and a - c <= d:
    print("Yes")

elif c > b > a and c - b <= d and b - a <= d:
    print("Yes")

elif a > b > c and a - b <= d and b - c <= d:
    print("Yes")

elif a == c:
    print("Yes")

else:
    print("No")