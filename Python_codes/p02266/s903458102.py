down = []
puddles = []
ans = 0

for i, s in enumerate(input()):
    if s == '\\':
        down.append(i)
    elif s == '/' and down:
        l = down.pop()
        # 累積和
        a = i - l
        # 高さが上から見ていった時下向きの斜面が今のペアの斜面より右にきている
        # -> 次の池
        while puddles and puddles[-1][0] > l:
            a += puddles.pop()[1]
        puddles.append((l, a))


print(sum(a for l, a in puddles))
print(len(puddles), *(a for l, a in puddles))
