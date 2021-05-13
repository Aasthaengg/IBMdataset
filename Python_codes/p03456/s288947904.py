a, b = input().split()

x = int(a + b)
if x ** 0.5 == int(x ** 0.5):
    print('Yes')
else:
    print('No')