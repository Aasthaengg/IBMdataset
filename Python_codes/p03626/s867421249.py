# ABC071D - Coloring Dominoes (ARC081D)
def main():
    """
    Vertical (V): a
                  a
    Horizontal (H): aa
                    bb
    """
    N = int(input())
    S1 = input().rstrip()
    S2 = input().rstrip()
    MOD = 10 ** 9 + 7
    a, b = S1[0], S2[0]
    ans = 3 if a == b else 6
    for i, j in zip(S1[1:], S2[1:]):
        if a != i and b != j:  # new dominos
            if a == b:  # V + H (2)
                ans *= 2
            else:  # H + V (1) or H + H (3)
                ans *= 1 if i == j else 3
            ans %= MOD
        a, b = i, j
    print(ans)


if __name__ == "__main__":
    main()