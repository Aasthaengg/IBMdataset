x = int(input())
n = x // 100
x %= 100
if n * 5 >= x:
    print(1)
else:
    print(0)