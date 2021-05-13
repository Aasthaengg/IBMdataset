def main():
    n = int(input())
    a_list = list(map(int, input().split()))
    sum_a = sum(a_list)
    min_val = 100
    min_index = 0

    for i, a in enumerate(a_list):
        d = abs(n * a - sum_a)
        if d < min_val:
            min_val = d
            min_index = i

    print(min_index)


if __name__ == "__main__":
    main()
