def main():
    s = list(input())
    K = int(input())

    s = list(map(lambda x: ord(x), s))
    B = [0 for _ in range(len(s))]
    for i in range(len(s)):
        b = 26 - (s[i] - ord("a"))
        if b == 26:
            B[i] = 0
        elif b <= K:
            K -= b
            B[i] = 0
        else:
            B[i] = b

    if K != 0:
        B[-1] -= K
        B[-1] %= 26

    ans = list(map(lambda c: chr(ord("a") + (26 - c) % 26), B))
    print("".join(ans))


main()
