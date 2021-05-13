def is_prime(x):
    if x < 2:
        return False
    i = 2
    while i * i <= x:
        if x % i == 0:
            return False
        i += 1
    return True


upper = 55555
count = {i: [] for i in range(5)}

for i in range(2, upper + 1):
    if is_prime(i):
        count[i % 5].append(i)

N = int(input())

ans = count[1][:N]
print(' '.join([str(a) for a in ans]))