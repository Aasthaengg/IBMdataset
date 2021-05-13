a, b = map(int, input().split())
print(a + b if b//a == b/a else b - a)