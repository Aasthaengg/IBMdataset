def main():
    S = map(int, input())

    a, b = 0, 1
    for s in S:
        a, b = a + s if a + s < b + 10 - s else b + 10 - s, a + (s + 1) if a + (s + 1) < b + 10 - (s + 1) else b + 10 - (s + 1)

    print(a)


main()