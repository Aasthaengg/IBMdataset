n = int(input())
min_val = 10 ** 12 + 1
i = 1
while i * i <= n:
    if n % i == 0:
        j = n // i
        val = i + j
        if min_val > val:
            min_val = val
    i += 1
print(min_val - 2)