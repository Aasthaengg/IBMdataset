def main():
    # n = int(input())
    # h, w, k = map(int, input().split())
    # a = list(map(int, input().split()))
    s = input()
    ans = ""
    for i in s:
        if i == "1":
            ans += "9"
        else:
            ans += "1"
    print(ans)


if __name__ == '__main__':
    main()
