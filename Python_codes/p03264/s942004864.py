
def main():
    k = int(input())
    if k % 2 == 1:
        print((k // 2 + 1) * (k // 2))
    else:
        print((k // 2) * (k // 2))


if __name__ == "__main__":
    main()
