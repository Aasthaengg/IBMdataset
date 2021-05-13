s = input()

st = len(s)
bk = 0
for i in range(len(s)):
    st = min(i, st) if s[i] == 'A' else st
    bk = max(i, bk) if s[i] == 'Z' else bk

print(bk - st + 1)
