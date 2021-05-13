a, b, c, d = list(map(int, input().split()))
if c >= a:
    if c - a <= d or b - a <= d and c - b <= d:
        print("Yes")
    else:
        print("No")
if c < a:
    if a - c < d or b - c <= d and a - b <= d:
        print("Yes")
    else:
        print("No")
