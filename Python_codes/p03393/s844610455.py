S = input()
N = len(S)
for c in "abcdefghijklmnopqrstuvwxyz":
    if c not in S:
        print(S + c)
        exit()

for i in range(N - 1, -1, -1):
    cur = ord(S[i]) - ord("a")
    for diff in range(1, 26):
        if cur + diff >= 26:
            continue
        nxt_c = chr(cur + diff + ord("a"))
        if nxt_c in S[:i]:
            continue
        print(S[:i] + nxt_c)
        exit()
else:
    print(-1)
