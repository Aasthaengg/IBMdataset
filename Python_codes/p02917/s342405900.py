def main():
    n = int(input())
    b = list(map(int, input().split()))
    a = [None] * n
    for i in range(n):
        if i == 0:
            a[i] = b[i]
        elif i <= n-2:
            a[i] = min(b[i-1], b[i])
        else:
            a[i] = b[i-1]
    ans = sum(a)
    print(ans)

if __name__ == '__main__':
    main()