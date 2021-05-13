S = input().strip()

tmp = S[0]
cnt = 0
for i in range(1, len(S)):
    if S[i] == tmp:
        continue
    else:
        tmp = S[i]
        cnt += 1

print(cnt)
