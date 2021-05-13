def read_values():
    return map(int, input().split())


def read_list():
    return list(read_values())


def main():
    N, i = read_values()
    print(N - i + 1)


if __name__ == "__main__":
    main()
