a, b, c, d = map(int, input().split())
a_c = abs(c - a)
a_b = abs(b - a)
b_c = abs(c - b)
if a_c <= d or (a_b <= d and b_c <= d):
    print("Yes")
else:
    print("No")