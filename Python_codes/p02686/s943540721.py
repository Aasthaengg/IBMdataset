def f_bracket_sequencing():
    N = int(input())
    Brackets = [input() for _ in range(N)]

    total = 0  # 正なら '(' が多い、負なら ')' が多い
    increase, decrease = [], []
    for s in Brackets:
        # 文字列を ±1 とみなして累積和を取ったとき、
        # ')' に対する '(' の多さの最終値と、それの最小値
        height, bottom = 0, 0
        for ch in s:
            height += 1 if ch == '(' else -1
            bottom = min(bottom, height)
        if height > 0:
            increase.append((bottom, height))
        else:
            decrease.append((bottom - height, -height))
        total += height
    increase.sort(reverse=True)
    decrease.sort(reverse=True)

    def accept(pairs):
        h = 0
        for p in pairs:
            b = h + p[0]
            if b < 0:
                return False  # '(' より ')' が多く、括弧列を構成できない
            h += p[1]
        return True

    return 'Yes' if accept(increase) and accept(decrease) and total == 0 else 'No'

print(f_bracket_sequencing())