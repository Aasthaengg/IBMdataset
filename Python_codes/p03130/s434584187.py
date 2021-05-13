def main(a_b: list):
    l = [0 for _ in range(4)]

    for a, b in a_b:
        l[a - 1] += 1
        l[b - 1] += 1

    if max(l) == 2:
        print('YES')
    else:
        print('NO')


if __name__ == "__main__":
    a_b = [list(map(int, input().split())) for _ in range(3)]

    main(a_b)
