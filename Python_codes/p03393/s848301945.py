S = input()

if len(S) != 26:
    chars = set()
    for s in S:
        chars.add(s)
    for c in range(ord('a'), ord('a') + 26):
        if chr(c) not in chars:
            print(S + chr(c))
            exit(0)

# len(S) == 26:
ans = S[0:25]
S = [ord(s) for s in S]
prev = [S[25]]
for i in range(24, -1, -1):
    res = 10000
    for p in prev:
        if S[i] < p:
            res = min(res, p)
    if res == 10000:
        prev.append(S[i])
    else:
        print(ans[0:i] + chr(res))
        exit(0)

print(-1)
