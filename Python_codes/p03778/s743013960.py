W, a, b = map(int, input().split())
if a + W < b:
    print(b - (a + W))
elif a - W <= b and b <= a + W:
    print('0')
else:
    print(a - (b + W))