def main():
    n = int(input())
    a_list = list(map(int, input().split()))
    b_list = list(map(int, input().split()))
    ans = 0

    for i in range(n):
        c = min(a_list[i], b_list[i])
        ans += c
        d = min(b_list[i] - c, a_list[i + 1])
        ans += d
        a_list[i + 1] -= d

    print(ans)


if __name__ == "__main__":
    main()
