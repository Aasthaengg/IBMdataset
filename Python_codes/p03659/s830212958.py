def main():
    input()
    t = list(map(int, input().split()))
    # if len(t) == 2:
    #     print(abs(t[0] - t[1]))
    #     exit()
    all = sum(t)
    left = t[0]
    right = all - t[0]
    ans = abs(left-right)
    for i in range(1, len(t)-1):
        left += t[i]
        if ans > abs(left-(all-left)):
            ans = abs(left-(all-left))
    print(ans)


if __name__ == '__main__':
    main()