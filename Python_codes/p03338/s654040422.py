def solve():
    N = int(input())
    S = input()
    ans = 0
    for i in range(1, N):
        cnt = 0
        for c in list(set(S[:i])):
            if c in list(set(S[i:])):
                cnt += 1
        ans = max(ans, cnt)
    print(ans)


if __name__ == "__main__":
    solve()