a, b, c = map(int, input().split())
print(a + b if a + b < b + c and a + b < c + a else (b + c if b + c < c + a else c + a))
