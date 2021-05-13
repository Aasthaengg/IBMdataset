def main(n: int, s_t: list, x: str):
    ans = 0
    i = 0

    for s, _ in s_t:
        i += 1
        if s == x:
            break

    for _, t in s_t[i:]:
        ans += int(t)

    print(ans)


if __name__ == "__main__":
    n = int(input())
    s = [input().split() for _ in range(n)]
    x = input()

    main(n, s, x)
