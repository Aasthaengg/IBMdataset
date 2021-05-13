def main():
    m = int(input())
    a = set(map(int, input().split()))
    n = int(input())
    b = set(map(int, input().split()))
    print(len(a & b))


if __name__ == "__main__":
    main()

