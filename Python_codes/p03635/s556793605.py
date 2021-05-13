# vim: set fileencoding=utf-8 :
def main():
    n, m = map(int, raw_input().split())

    if n >= 2 and m >= 2:
        print((n-1)*(m-1))


if __name__ == "__main__":
    main()
