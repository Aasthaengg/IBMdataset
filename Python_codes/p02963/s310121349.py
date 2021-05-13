def main():
    s = int(input())
    p, q = divmod(-s, 10 ** 9)
    print(0, 0, 1, 10 ** 9, abs(p), q)


if __name__ == '__main__':
    main()
