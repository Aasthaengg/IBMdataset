def main():
    a, b = input(), input()
    len_a, len_b = len(a), len(b)

    if len_a < len_b:
        print("LESS")
    elif len_a > len_b:
        print("GREATER")
    else:
        if a < b:
            print("LESS")
        elif a > b:
            print("GREATER")
        else:
            print("EQUAL")


if __name__ == "__main__":
    main()
