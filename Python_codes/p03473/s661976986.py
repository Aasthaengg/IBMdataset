def read_values():
    return map(int, input().split())


def read_list():
    return list(read_values())


def main():
    M = int(input())
    print(48 - M)


if __name__ == "__main__":
    main()
