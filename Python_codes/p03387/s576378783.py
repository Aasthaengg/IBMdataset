num = list(input().split())
num = sorted([int(num[i]) for i in range(3)])

a = num[2] - num[1]
b = (num[2] - a - num[0]) % 2
c = (num[2] - a - num[0]) // 2

if b == 1:
    print(a + c + 2)
else:
    print(a + c)
