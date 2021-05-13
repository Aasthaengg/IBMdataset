def main():
    a, b = get_params()
    print(answer(a, b))


def get_params():
    return map(int, input().split())


def answer(a, b):
    return a+b if b % a == 0 else b-a


if __name__ == "__main__":
    main()
