def main():
    a, b = input().split()

    ans = min(a * int(b), b * int(a))

    print(ans)


if __name__ == "__main__":
    main()
