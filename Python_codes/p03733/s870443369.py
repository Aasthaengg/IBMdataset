def main():
    N, T = map(int, input().split())
    *t, = map(int, input().split())
    t += [1 << 31]

    u = iter(t)
    next(u)

    ans = sum(min(T, u_ - t_) for t_, u_ in zip(t, u))
    print(ans)


if __name__ == '__main__':
    main()
