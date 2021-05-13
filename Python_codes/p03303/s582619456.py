def main(s: str, w: int):
    print(s[::w])


if __name__ == "__main__":
    s = input()
    w = int(input())

    main(s, w)
