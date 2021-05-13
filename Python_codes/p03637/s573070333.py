n = int(input())
a = list(map(int, input().split()))

num1, num2, num4 = 0, 0, 0
for i in a:
    if i % 4 == 0:
        num4 += 1
    elif i % 2 == 0:
        num2 += 1
    else:
        num1 += 1

if num1 <= num4:
    print('Yes')
elif num1 == num4 + 1 and num2 == 0:
    print('Yes')
else:
    print('No')