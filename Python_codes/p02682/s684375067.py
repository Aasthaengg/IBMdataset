def main():
    a, b, c, k = (int(i) for i in input().split())
    ans = min(a, k)
    k -= a
    if k <= 0:
        print(ans)
        return
    k -= b
    if k <= 0:
        print(ans)
        return
    print(ans - k)


if __name__ == '__main__':
    main()
