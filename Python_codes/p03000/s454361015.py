def main():
    N, X = map(int, input().split())
    L = map(int, input().split())
    d = 0
    ans = 1
    for l in L:
        d += l
        if d <= X:
            ans += 1
        else:
            break
    print(ans)


if __name__ == '__main__':
    main()
