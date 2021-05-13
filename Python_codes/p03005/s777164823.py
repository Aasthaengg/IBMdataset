def input_from_console():
    n, k = map(int, input().split())
    return n, k


def solve(n, k):
    if k == 1:
        return 0
    return n - k


def main():
    n, k = input_from_console()
    print(solve(n, k))


if __name__ == "__main__":
    import sys

    if sys.gettrace():  # Check if the python interpreter is in debug mode or not.
        check_cases()
    else:
        main()
