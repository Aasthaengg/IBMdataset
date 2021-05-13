def main():
    n = int(input())
    a = list(map(int, input().split()))
    all_v = sum(a)
    ans = 0
    if n == 0:
        if a[0] == 1:
            ans = 1
        else:
            ans = -1
    elif a[0] != 0:
        ans = -1
    else:
        ans = 1
        max_vertex = 1
        for i in range(1, n + 1):
            max_vertex *= 2
            if max_vertex < a[i]:
                ans = -1
                break
            ans += min(max_vertex, all_v)
            max_vertex = min(max_vertex, all_v) - a[i]
            all_v -= a[i]
    print(ans)


if __name__ == '__main__':
    main()
