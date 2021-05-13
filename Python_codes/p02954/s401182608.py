def agg(li):
    LEN = len(li)
    agged = [0] * 2
    if LEN % 2:
        agged[0] = (LEN + 1) // 2
        agged[1] = LEN // 2
    else:
        agged[0] = agged[1] = LEN // 2
    for i in range(LEN - 1):
        if li[i + 1] != li[i]:
            if i % 2:
                return [0] * i + agged[::-1] + [0] * (LEN - i - 2)
            else:
                return [0] * i + agged + [0] * (LEN - i - 2)
    return


S = input()
N = len(S)

ans = []
chunk = [S[0]]
for i in range(N - 1):
    if S[i] == 'L' and S[i + 1] == 'R':
        ans += agg(chunk)
        chunk = [S[i + 1]]
    else:
        chunk.append(S[i + 1])
ans += agg(chunk)
print(' '.join(map(str, ans)))
