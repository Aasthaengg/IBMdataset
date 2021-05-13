def resolve():
    n = int(input())
    s = input()
    print("Yes" if s.count("R") > n / 2 else "No")


if __name__ == "__main__":
    resolve()
