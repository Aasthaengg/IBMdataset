S = input()
prev = S[0]
cnt = 0
for c in S[1:]:
    if c == prev:
        continue
    prev = c
    cnt += 1
print(cnt)
