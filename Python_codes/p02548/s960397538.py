num = int(input())
tot = 0
i = 1
while i < num:
    if num % i == 0:
        i2 = num / i - 1
    else:
        i2 = int(num / i)
    tot += i2
    i += 1
print(int(tot))