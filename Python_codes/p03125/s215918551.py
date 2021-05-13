a, b = map(int, input().split())
num = b/a
if num.is_integer():
    print(a+b)
else:
    print(b-a)
