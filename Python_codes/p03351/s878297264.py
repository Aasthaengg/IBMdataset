a, b, c, d = map(int, input().split())
# abs関数で引数を絶対値とする。

if abs(c - a) > d:
    if abs(a - b) > d or abs(b - c) > d:
        print("No")
    else:
        print("Yes")
else:
    print("Yes")


