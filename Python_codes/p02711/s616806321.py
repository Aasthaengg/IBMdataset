n = int(input())

while n > 0:
    if n % 10 == 7:
        print('Yes')
        break
    n = n // 10
else:
    print('No')