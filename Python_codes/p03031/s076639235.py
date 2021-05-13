def main():
    N, M = map(int, input().split())
    S = []
    for _ in range(M):
        S.append(set(list(map(int, input().split()))[1:]))
    P = list(map(int, input().split()))

    ans = 0
    for bit in range(1 << N):
        on_switches = set([])
        for i in range(N):
            if bit & (1 << i):
                on_switches.add(i + 1)

        flag = True
        for s, p in zip(S, P):
            if len(s & on_switches) % 2 != p:
                flag = False
        if flag is True:
            ans += 1
    print(ans)


if __name__ == '__main__':
    main()