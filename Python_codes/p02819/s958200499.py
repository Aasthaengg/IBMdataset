def make_divisors(n):
    divisors = set()
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            divisors.add(i)
            if i != n // i:
                divisors.add(n//i)
    return divisors

X = int(input())
for i in range(X,99992):
    if len(make_divisors(i)) == 2:
        print(i)
        break
else:
    print(100003)