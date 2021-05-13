def main():
    n, k = map(int, input().split())
    h = list(map(int, input().split()))

    if n <= k:
        print(0)
    else:
        h.sort(reverse=True)
        print(sum(h[k:]))

if __name__ == '__main__':
    main()