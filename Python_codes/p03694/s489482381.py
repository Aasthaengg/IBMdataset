def main():
    n = int(input())
    a_list = list(map(int, input().split()))

    print(max(a_list) - min(a_list))


if __name__ == "__main__":
    main()
