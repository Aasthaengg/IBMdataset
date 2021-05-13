
def main():
    n = int(input())
    a = list(map(int, input().split()))
    ans = 0
    k = 10001
    for i in range(n - 2):
        if a[i] == a[i + 1] and a[i + 1] == a[i + 2]:
            ans += 1
            a[i + 1] = k
            k += 1
    for i in range(n - 1):
        if a[i] == a[i + 1]:
            ans += 1
            a[i + 1] = k
            k += 1
    print(ans)


if __name__ == '__main__':
    main()
