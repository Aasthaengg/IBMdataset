import sys


def next_str() -> str:
    result = ""
    while True:
        tmp = sys.stdin.read(1)
        if tmp.strip() != "":
            result += tmp
        elif tmp != '\r':
            break
    return result


def next_int() -> int:
    return int(next_str())


def main() -> None:
    n, a, b = [next_int() for _ in range(3)]

    if (b - a) % 2 == 0:
        print("Alice")
    else:
        print("Borys")


if __name__ == '__main__':
    main()