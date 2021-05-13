def main():
    S = input()
    T = S[::-1]

    cnt = 0
    for s_, t_ in zip(S, T):
        if s_ != t_:
            cnt += 1

    cnt //= 2

    print(cnt)


if __name__ == '__main__':
    main()
