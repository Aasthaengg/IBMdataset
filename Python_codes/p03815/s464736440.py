def resolve():
    n = int(input())

    if n <= 6:
        return print(1)
    elif n <= 11:
        return print(2)
    else:
        c = n // 11
        MOD = 2 if n % 11 > 6 else 1
        if n % 11 == 0:
            MOD = 0
    print(c*2+MOD)

if __name__ == '__main__':
    resolve()
