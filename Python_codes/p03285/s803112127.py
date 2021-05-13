s = input()
n = int(s)

price = 0
in_four = 0
in_seven = 0
check = False

for i in range(30):
    price = 0
    price += i * 4
    if price == n:
        check = True
        break
    for j in range(20):
        price += j * 7
        if price == n:
            check = True
            break
        if price > n:
            break

if check:
    print('Yes')
else:
    print('No')