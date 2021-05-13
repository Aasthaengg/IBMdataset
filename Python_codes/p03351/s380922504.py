a, b, c, d = map(int, input().split())

c2a = abs(c-a)
c2b = abs(c-b)
b2a = abs(b-a)

if c2a <= d or c2b <= d and b2a <= d:
    print("Yes")
else:
    print("No")
