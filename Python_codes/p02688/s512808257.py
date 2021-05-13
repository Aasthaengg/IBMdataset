def main(n, k):
    no_sweet = [x + 1 for x in range(n)]
    for _ in range(k):
        input()
        for v in map(int, input().split()):
            if v in no_sweet:
                no_sweet.remove(v)
    print(len(no_sweet))


if __name__ == "__main__":
    n, k = map(int, input().split())
    main(n, k)
