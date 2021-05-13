n = int(input())
if n == 1:
    print("Hello World")
else:
    a,b = map(int, [input() for i in range(2)])
    print(a + b)