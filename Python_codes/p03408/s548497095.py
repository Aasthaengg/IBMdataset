def solve():
    N = int(input())
    s = []
    for _ in range(N):
        s.append(input())
    M = int(input())
    t = []
    for _ in range(M):
        t.append(input())

    ans = 0
    for s_i in s:
        tmp = 0
        tmp += s.count(s_i)
        tmp -= t.count(s_i)
        ans = max(ans, tmp)
    print(ans)


if __name__ == "__main__":
    solve()
