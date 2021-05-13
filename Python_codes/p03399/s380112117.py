url = "https://atcoder.jp/contests/abc092/tasks/abc092_a"

def main():
    ans = 0
    t = []
    for i in range(2):
        t.append(int(input()))
    ans = min(t)
    t = []
    for i in range(2):
        t.append(int(input()))
    ans += min(t)
    print(ans)


if __name__ == '__main__':
    main()


