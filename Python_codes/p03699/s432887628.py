def solve():
    N = int(input())
    s = [int(input()) for _ in range(N)]
    s.sort()
    ans = sum(s)

    if ans % 10 != 0:
        print(ans)
        return

    mn = float('inf')
    for i in range(N):
        if s[i] % 10 != 0:
            mn = min(mn, s[i])
    
    if mn == float('inf'):
        print(0)
    else:
        ans -= mn
        print(ans)

if __name__ == '__main__':
    solve()