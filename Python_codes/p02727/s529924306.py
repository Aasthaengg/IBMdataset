def main():
    X, Y, A, B, C = map(int, input().split())
    p = list(map(int, input().split()))
    q = list(map(int, input().split()))
    r = list(map(int, input().split()))

    p.sort(reverse=True)
    q.sort(reverse=True)
    r.sort(reverse=True)

    p = p[:X]
    q = q[:Y]

    apple = list()
    apple.extend(p)
    apple.extend(q)
    apple.extend(r)

    apple.sort(reverse=True)
    ans = 0
    for i in range(X+Y):
        ans += apple[i]

    print(ans)


if __name__ == "__main__":
    main()
