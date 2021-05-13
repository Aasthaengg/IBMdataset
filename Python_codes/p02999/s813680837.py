def main():
    X, A = (int(x) for x in input().split())
    if X >= A:
        print(10)
    else:
        print(0)


if __name__ == "__main__":
    main()
