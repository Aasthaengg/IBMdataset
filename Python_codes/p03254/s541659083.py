# vim: fileencoding=utf-8


def main():
    n, x = map(int, input().split())
    li = list(map(int, input().split()))
    li.sort()
    ans = 0
    for i in range(len(li)):
        x = x - li[i]
        if x < 0:
            break
        ans += 1
    if x > 0:
        ans -= 1
    print(ans)


if __name__ == "__main__":
    main()
