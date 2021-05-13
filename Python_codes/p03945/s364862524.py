S = input().strip()
cur = S[0]
cnt = 0
for i in range(1,len(S)):
    if S[i]==cur:continue
    else:
        cnt += 1
        cur = S[i]
print(cnt)