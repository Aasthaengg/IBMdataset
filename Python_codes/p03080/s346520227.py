# exawizards2019B - Red or Blue
def main():
    n = int(input())
    S = input()
    print("Yes" if S.count("R") > S.count("B") else "No")


if __name__ == "__main__":
    main()