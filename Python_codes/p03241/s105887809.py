def main():
    n, m = map(int, input().split())
    f = [1, m]
    i = 2
    while i * i <= m:
        if m % i == 0:
            f.append(i)
            if m != i * i:
                f.append(m // i)
        i += 1
    f.sort()
    answer = 0
    for ff in f:
        if n <= ff:
            answer = m // ff
            break
    print(answer)


if __name__ == '__main__':
    main()

