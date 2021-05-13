def main():
    n = int(input())
    s = input()

    r = s.count("R")
    b = n - r

    if r > b:
        print("Yes")
    else:
        print("No")


if __name__ == "__main__":
    main()
