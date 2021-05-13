def main():
    n = int(input())
    a_list = list(map(int, input().split()))
    total_length = sum(a_list)
    ans = total_length
    accum_length = 0

    for i in range(n):
        accum_length += a_list[i]
        ans = min(ans, abs(2 * accum_length - total_length))

    print(ans)


if __name__ == "__main__":
    main()
