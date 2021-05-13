a, b, c = map(int, input().split())

if a == b and b == c:
    print(a + b)
else:
    list_price = [a, b, c]
    print(sorted(list_price)[0] + sorted(list_price)[1])