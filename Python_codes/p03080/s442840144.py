def main():
    N = int(input())
    S = input()
    if S.count("R") > S.count("B"):
        print("Yes")
    else:
        print("No")


if __name__ == '__main__':
    main()
