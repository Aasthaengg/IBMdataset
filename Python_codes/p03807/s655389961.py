def main():
    N = int(input())
    A = list(map(int, input().split()))

    odd_even = {"odd": 0, "even": 0}

    for num in A:
        if num % 2 == 0:
            odd_even["even"] += 1
        else:
            odd_even["odd"] += 1

    if odd_even["odd"] % 2 == 0:
        print("YES")
    else:
        print("NO")


if __name__ == "__main__":
    main()
