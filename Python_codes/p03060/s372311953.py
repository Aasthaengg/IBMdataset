def main():
    n = int(input())
    v_list = list(map(int, input().split()))
    c_list = list(map(int, input().split()))
    ans = 0

    for i in range(n):
        if v_list[i] > c_list[i]:
            ans += v_list[i] - c_list[i]

    print(ans)


if __name__ == "__main__":
    main()
