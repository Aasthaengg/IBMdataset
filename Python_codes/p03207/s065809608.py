def main():
    n = int(input())
    p_list = [int(input()) for _ in range(n)]
    p_list.sort()
    p_list[n - 1] //= 2

    print(sum(p_list))


if __name__ == "__main__":
    main()
