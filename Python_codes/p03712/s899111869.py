def main():
    h, w = map(int, input().split())
    a_list = [input() for _ in range(h)]

    print("#" * (w + 2))
    for a in a_list:
        print("#" + a + "#")
    print("#" * (w + 2))


if __name__ == "__main__":
    main()
