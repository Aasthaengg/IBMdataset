N = int(input())
S = input()

sl_E = []
sl_W = []
for i, s in enumerate(S):
    E = 1 if s == "E" else 0
    W = 1 if s == "W" else 0
    s_E = sl_E[i - 1] + E if i != 0 else E
    s_W = sl_W[i - 1] + W if i != 0 else W
    sl_E.append(s_E)
    sl_W.append(s_W)

_min = sl_E[-1]
for i in range(1, N):
    count = sl_W[i - 1]
    count += sl_E[-1] - sl_E[i]
    if count < _min:
        _min = count

print(_min)
