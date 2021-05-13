def main():
    from collections import deque

    N, L = map(int, input().split())
    *a, = map(int, input().split())

    def solve(a):
        dq = deque()
        s = 0
        ans = 0
        for x in a:
            if len(dq) > 1:
                t = dq.popleft()
                s -= t
            eat = max(0, s + x - L)
            if eat:
                x -= eat
                ans += eat
            s += x
            dq.append(x)
        return ans

    ans =solve(a) # reversed(a)確認しないとどうなるか

    print(ans)


if __name__ == '__main__':
    main()
