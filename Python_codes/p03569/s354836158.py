def main() -> None:
    S = input()
    N = len(S)
    pos = []
    ss = []
    for i, s in enumerate(S):
        if s != 'x':
            ss.append(s)
            pos.append(i)
    if ss != ss[::-1]:
        print(-1)
        return

    L = len(ss)
    if len(ss) == 0:
        print(0)
        return
    if L % 2 == 0:
        left, right = (L-1) // 2, L // 2
    else:
        left = right = L // 2
    left, right = left - 1, right + 1
    ans = 0
    while left >= 0 and right < L:
        ans += abs((pos[left + 1] - pos[left] - 1) -
                   (pos[right] - pos[right-1] - 1))
        left, right = left - 1, right + 1
    ans += abs((pos[0] - 0) - (N - 1 - pos[-1]))
    print(ans)


if __name__ == '__main__':
    main()
