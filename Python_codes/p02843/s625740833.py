x = int(input())

canbuy = x // 100
amari = x % 100

num = amari // 5
amari %= 5
if amari != 0:
    num += 1

if num <= canbuy:
    print(1)
else:
    print(0)
