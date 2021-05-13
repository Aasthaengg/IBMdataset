def main():
    x, y = input().split()

    x_ord, y_ord = ord(x), ord(y)
    if x_ord < y_ord:
        ans = "<"
    elif x_ord > y_ord:
        ans = '>'
    else:
        ans = '='
    print(ans)


if __name__ == "__main__":
    main()
