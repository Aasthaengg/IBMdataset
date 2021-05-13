def main():
    R = int(input())
    ans = "ABC" if R < 1200 else "ARC" if R < 2800 else "AGC"
    print(ans)


if __name__ == "__main__":
    main()
