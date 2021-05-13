N = int(input())

price = int(N / 1.08)
if int(price * 1.08) == N:
    print(price)
elif int((price + 1) * 1.08) == N:
    print(price + 1)
else:
    print(':(')