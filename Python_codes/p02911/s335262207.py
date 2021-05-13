def main():
    n, k, q = map(int, input().split())
    a_list = [0 for _ in range(n)]

    for _ in range(q):
        a = int(input())
        a_list[a - 1] += 1

    if k > q:
        for _ in range(n):
            print("Yes")
        exit()

    for a in a_list:
        if a < q - k + 1:
            print("No")
        else:
            print("Yes")


if __name__ == "__main__":
    main()
