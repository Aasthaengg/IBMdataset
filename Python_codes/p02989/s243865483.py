def main():
    n = int(input())
    d = list(map(int, input().split()))

    sort_d = sorted(d)

    median_index = int(n/2)

    median_d = sort_d[median_index]
    median_d_minus1 = sort_d[median_index-1]

    answer = median_d - median_d_minus1
    print(answer)


if __name__ == '__main__':
    main()