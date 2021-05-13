def main():
    n, k = map(int, input().split())
    p_lst = list(map(int, input().split()))

    p_lst.sort()

    print(sum(p_lst[:k]))


if __name__ == "__main__":
    main()
