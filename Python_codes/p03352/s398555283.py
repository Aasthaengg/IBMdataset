x = int(input())
if x == 1:
    print(1)
elif x == 1000:
    print(1000)
else:
    print(int(max(int((x ** (1 / i))) ** i for i in range(2, x + 1))))
