# -*- coding: utf-8 -*-
S = input()

buf = [[0]]
for i in range(1, len(S)):
    buf2 = [b + [i] for b in buf] + buf
    buf = buf2
buf = [b + [len(S)] for b in buf]

ans = 0
for b in buf:
    for i in range(len(b) - 1):
        right, left = b[i], b[i+1]
        ans += int(S[right: left])
print(ans)
