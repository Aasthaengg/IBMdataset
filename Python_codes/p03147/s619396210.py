def main():
    n = int(input())
    h = list(map(int, input().split()))
    ans = h[0]
    for i in range(n-1):
        if h[i+1] > h[i]:
            ans += h[i + 1]-h[i]
    print(ans)


if __name__ == '__main__':
    main()
