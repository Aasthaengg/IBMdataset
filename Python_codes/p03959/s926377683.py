def solve(n, aaa, bbb):
    # 最大値が更新された=その山の高さは決定
    max_heights = [0] * n
    fixed = [False] * n
    MOD = 10 ** 9 + 7

    h = 0
    for i, a in enumerate(aaa):
        if h != a:
            max_heights[i] = a
            fixed[i] = True
        else:
            max_heights[i] = a
        h = a
        
    h = 0
    for i, b in reversed(list(enumerate(bbb))):
        if h != b:
            if max_heights[i] < b:
                return 0
            if fixed[i] and max_heights[i] != b:
                return 0
            max_heights[i] = b
            fixed[i] = True
        else:
            max_heights[i] = min(max_heights[i], b)
        h = b

    ans = 1
    for h, f in zip(max_heights, fixed):
        if f:
            continue
        ans = ans * h % MOD
    return ans


n = int(input())
aaa = list(map(int, input().split()))
bbb = list(map(int, input().split()))
print(solve(n, aaa, bbb))
