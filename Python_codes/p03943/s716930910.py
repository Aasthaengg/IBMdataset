a, b, c = map(int, input().split())
flag = any([
    a + b == c,
    b + c == a,
    c + a == b
])
print('Yes' if flag else 'No')