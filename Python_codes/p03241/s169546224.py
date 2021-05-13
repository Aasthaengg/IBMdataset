def main():
    N, M = map(int, input().split())

    st = {1, M}
    d = 2
    while d * d <= M:
        if M % d == 0:
            st.add(d)
            st.add(M // d)
        d += 1

    ans = 1
    for d in st:
        if d >= N:
            e = M // d
            ans = max(ans, e)
    print(ans)


if __name__ == '__main__':
    main()
