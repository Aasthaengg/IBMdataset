x = int(input())
count = x // 11
count2 = x % 11

if count2 == 0:
    print(count * 2)
elif count2 <= 6:
    print(count * 2 + 1)
else:
    print(count * 2 + 2)
