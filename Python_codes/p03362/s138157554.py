def is_prime(n):
    if n < 2:
        return False
    else:
        for p in range(2, n):
            if n % p == 0:
                return False
        else:
            return True


# input
N = int(input())

# check
prime_nums = []
append = prime_nums.append
for n in range(2, 55555):
    if is_prime(n) and n % 5 == 1:
        append(n)
        if len(prime_nums) == N:
            break

res = " ".join([str(num) for num in prime_nums])
print(res)
exit(0)