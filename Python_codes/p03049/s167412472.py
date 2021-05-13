def main():
    N = int(input())
    S = [input() for _ in range(N)]
    # B***
    # ***A
    # B**A
    c_a, c_b, c_ba = 0, 0, 0
    ans = 0
    for s in S:
        if s[0] == 'B' and s[-1] == 'A':
            c_ba += 1
        elif s[-1] == 'A':
            c_a += 1
        elif s[0] == 'B':
            c_b += 1
        ans += len(s.split('AB')) - 1
    ans += max(0, c_ba - 1)
    if c_ba > 0:
        if c_a > 0:
            c_a -= 1
            ans += 1
        if c_b > 0:
            c_b -= 1
            ans += 1
    ans += min(c_a, c_b)
    print(ans)


if __name__ == '__main__':
    main()