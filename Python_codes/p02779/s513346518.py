def solve():
    n = int(input())
    s = list(map(int, input().split()))
    t = set(s)
    print("YES" if len(s) == len(t) else "NO")


solve()
