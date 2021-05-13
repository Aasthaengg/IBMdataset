def main():
    N = int(input())
    H = list(map(int, input().split())) + [10**9 + 1]
    ans = t = c = 0
    for h in H:
        if h <= t:
            c += 1
        else:
            ans = max(ans, c)
            c = 0
        t = h
    print(ans)

if __name__ == '__main__':
    main()
