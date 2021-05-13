def main():
    S = map(int, input())

    a, b = 0, 1
    for s in S:
        a, b = min(a + s, b + 10 - s), min(a + (s + 1), b + 10 - (s + 1))

    print(a)


main()