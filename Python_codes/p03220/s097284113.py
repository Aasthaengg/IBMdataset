def main():
    n = int(input())
    t, a = map(int, input().split())
    h = list(map(int, input().split()))
    # s = input()

    mini = 10**10
    ans = 0
    for i, x in enumerate(h):
        c = t - x * 0.006
        if abs(a - c) < mini:
            mini = abs(a - c)
            ans = i+1

    print(ans)


if __name__ == '__main__':
    main()
