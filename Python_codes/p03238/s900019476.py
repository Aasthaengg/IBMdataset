n = int(input())

if n == 1:
    print('Hello World')
    exit()
else:
    a = list([input() for i in range(2)])
    print(int(a[0])+int(a[1]))
