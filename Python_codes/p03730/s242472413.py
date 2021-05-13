def main():
    A, B, C = map(int, input().split())

    rs = [0] * B
    r = A % B

    s = r
    while True:
        if rs[s]: break
        rs[s] = 1
        s = (s + r) % B

    print('YES' if rs[C] else 'NO')


if __name__ == '__main__':
    main()
