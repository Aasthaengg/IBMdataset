def divisor(n): 
    i = 1
    table = []
    while i * i <= n:
        if n % i == 0:
            table.append(i)
            table.append(n//i)
        i += 1
    table = list(set(table))
    return table

N = int(input())
total = 0

for n in range(1, N + 1, 2):
    if len(divisor(n)) == 8:
        total += 1

print(total)