def solve():
    S = input()
    ans = 0
    B_cnt = 0
    for s in S:
        if s == 'W':
            ans += B_cnt
        else:
            B_cnt += 1
    print(ans)


if __name__ == "__main__":
    solve()