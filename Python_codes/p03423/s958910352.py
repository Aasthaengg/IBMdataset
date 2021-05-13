num = int(input())

num2 = num % 3

if num < 3:
    print('0')
elif num2 < 0:
    print(num // 3 + 1)
else:
    print(num // 3)