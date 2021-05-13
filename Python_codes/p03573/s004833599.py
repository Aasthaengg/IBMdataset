a, b, c = map(int, input().split())
if (a != b and b != c and c == a):
    print(b)
elif (a == b and b != c and c != a):
    print(c)
elif (a != b and b == c and c != a):
    print(a)
