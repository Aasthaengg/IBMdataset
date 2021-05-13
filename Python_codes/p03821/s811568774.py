def main():
    N = int(input())
    nums_list = [list(map(int, input().split())) for _ in range(N)]
    nums_list.reverse()
    cnt = 0
    for a, b in nums_list:
        cnt += (b - (a + cnt)) % b
    print(cnt)


if __name__ == '__main__':
    main()
