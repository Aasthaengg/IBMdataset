n = 100000
for i in range(int(input())):
    n *= 1.05;
    if n % 1000:
        n += 1000
    n = int(n / 1000) * 1000
print(n)