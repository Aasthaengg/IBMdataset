S = input()
N = len(S)
ans = 0
cnt = 0

for i in range(N):
    if S[i] == 'T':
        cnt += 1
    else:
        cnt -= 1
    ans = max(ans,cnt)

print(ans * 2)