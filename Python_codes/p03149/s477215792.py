def main():
    n_list = list(map(int, input().split()))
    n_list.sort()

    if n_list == [1, 4, 7, 9]:
        print("YES")
    else:
        print("NO")


if __name__ == "__main__":
    main()
