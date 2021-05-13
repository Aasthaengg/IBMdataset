def main():
    n = int(input())
    a_list = list(map(int, input().split()))
    ans_list = [0] * n

    for i in range(n):
        ans_list[a_list[i] - 1] = i + 1

    for ans in ans_list:
        print(ans, end=" ")


if __name__ == "__main__":
    main()
