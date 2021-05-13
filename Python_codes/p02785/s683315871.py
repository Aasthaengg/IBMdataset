def main():
    n, k = map(int, input().split())
    h = [int(x) for x in input().split()]
    h_s = sorted(h)
    if len(h_s) <= k:
        ans = 0
    else:
        for _ in range(k):
            h_s.pop()
        ans = sum(h_s)
    print(ans)

if __name__ == '__main__':
    main()