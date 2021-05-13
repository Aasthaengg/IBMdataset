x = int(input())

deposit = 100

i = 1

while True:
    deposit += deposit // 100

    if deposit >= x:
        break

    i += 1

print(i)
