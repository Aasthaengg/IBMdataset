def main():
    MOD = 10 ** 9 + 7
    L = input()
    a, b = 0, 1
    for i in L:
        if i == '1':
            a, b = (b + a * 2) % MOD, b * 3 % MOD
        else:
            a, b = (a * 3) % MOD, (b + a * 2) % MOD
    return b

print(main())
