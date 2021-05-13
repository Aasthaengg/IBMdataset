coin500 = int(input())
coin100 = int(input())
coin50 = int(input())
price = int(input())

count = 0

i = 0
while i <= coin500:
    j = 0
    while j <= coin100:
        k = 0
        while k <= coin50:
            if i * 500 + j * 100 + k * 50 == price:
                count += 1
            k += 1
        j += 1
    i += 1

print(count)
