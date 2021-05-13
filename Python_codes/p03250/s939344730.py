a, b, c = map(int, input().split())
max_num = max(a, b, c)
if max_num == a:
    X = int(str(a) + str(b))
    print(X + c)
elif max_num == b:
    X = int(str(b) + str(a))
    print(X + c)
elif max_num == c:
    X = int(str(c) + str(a))
    print(X + b)
