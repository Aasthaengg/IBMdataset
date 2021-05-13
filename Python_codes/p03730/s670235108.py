def main():
    a, b, c = map(int, input().split())
    mod = []
    mul_a = a
    while True:
        if mul_a % b == 0:
            break
        else:
            mod.append(mul_a % b)
            mul_a += a

    if c in mod:
        print('YES')
    else:
        print('NO')

if __name__ == '__main__':
    main()    