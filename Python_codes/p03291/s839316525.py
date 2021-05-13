def main():
    S = input()
    mod = 10 ** 9 + 7
    A = AB = ABC = 0
    n = 1
    for i in S:
        if i == '?':
            ABC = ABC * 3 + AB
            AB = AB * 3 + A
            A = A * 3 + n
            n = n * 3 % mod
        if i == 'C':
            ABC = ABC + AB
        if i == 'B':
            AB = AB + A
        if i == 'A':
            A += n
    print(ABC % mod)

main()
