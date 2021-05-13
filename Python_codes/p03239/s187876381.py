def main():
    # n = int(input())
    n, t = map(int, input().split())
    # a = list(map(int, input().split()))
    # s = input()
    ct = []
    for _ in range(n):
        ct.append(list(map(int, input().split())))

    mini = 10**10
    for i in range(n):
        if ct[i][1] <= t and ct[i][0] < mini:
            mini = ct[i][0]

    if mini == 10**10:
        print("TLE")
    else:
        print(mini)


if __name__ == '__main__':
    main()
