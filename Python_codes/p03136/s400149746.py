def main():
    n = int(input())
    l = list(map(int, input().split()))

    max_l = max(l)
    l.remove(max_l)

    sum_exc_l = sum(l)

    if max_l < sum_exc_l:
        print("Yes")
    else:
        print("No")


if __name__ == "__main__":
    main()
