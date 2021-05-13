# AGC030A - Poisonous Cookies
def main():
    a, b, c = list(map(int, input().rstrip().split()))
    if c > b:
        print(b * 2 + 1 + min(a, c - b - 1))
    else:
        print(b + c)


if __name__ == "__main__":
    main()