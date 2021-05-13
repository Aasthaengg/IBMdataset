def main():
    # n = int(input())
    # t, a = map(int, input().split())
    # h = list(map(int, input().split()))
    s = input()
    mini = 10**10
    for i in range(len(s)-2):
        mini = min(mini, abs(int(s[i:i+3]) - 753))

    print(mini)


if __name__ == '__main__':
    main()
