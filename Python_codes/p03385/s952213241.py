def main():
    S = input()
    if "".join(sorted(S)) == "abc":
        print("Yes")
    else:
        print("No")


if __name__ == '__main__':
    main()
