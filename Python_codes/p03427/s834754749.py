def main():
    n = input()
    len_n = len(n)
    if n[1:] == "9" * (len_n - 1):
        print(int(n[0]) + 9 * (len_n - 1))
    else:
        print(int(n[0]) + 9 * (len_n - 1) - 1)


if __name__ == "__main__":
    main()
