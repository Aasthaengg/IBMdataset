def divG(n) -> list:
    if n == 0:
        return [0]
    i = 1
    table = set()
    while i * i <= n:
        if n % i == 0:
            table |= {(n // i - 1) * (i < n // i - 1)}
        i += 1
    return table
print(sum(divG(int(input()))))