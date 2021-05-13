from bisect import bisect_right


def main():
    n = int(input())
    a = sorted(list(map(int, input().split())))
    b = sorted(list(map(int, input().split())))
    c = sorted(list(map(int, input().split())))
    l = [0] * n
    for index, i in enumerate(b):
        l[index] = n - bisect_right(c, i)
    s = [l[-1]] * n
    for i in range(n - 2, -1, -1):
        s[i] = s[i + 1] + l[i]
    ans = 0
    for i in a:
        j = bisect_right(b, i)
        if j < n:
            ans += s[j]
    print(ans)


if __name__ == '__main__':
    main()
