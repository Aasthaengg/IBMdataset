S = input().strip()
N = len(S)
cur = 0
cnt = 0
for i in range(1,N):
    if S[i]!=S[cur]:
        cnt += 1
        cur = i
print(cnt)