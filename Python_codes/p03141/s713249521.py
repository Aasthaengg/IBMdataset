def main():
    n = int(input())
    A = []
    for _ in range(n):
        a, b = list(map(int, input().split()))
        A.append([a, b, a + b])
    A.sort(key = lambda x: x[2], reverse = True)
    ans = 0
    for i, a in enumerate(A):
        if i % 2 == 0:
            ans += a[2]
        ans -= a[1]
    print(ans)


if __name__ == '__main__':
    main()
