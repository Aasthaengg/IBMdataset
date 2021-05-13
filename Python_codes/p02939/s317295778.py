S = input()
cnt = 1
now = S[0]
tmp = ""
for s in S[1:]:
    tmp += s
    if now != tmp:
        cnt += 1
        now = tmp
        tmp = ""

print(cnt)
