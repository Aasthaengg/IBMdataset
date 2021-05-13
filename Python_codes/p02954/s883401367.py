S = input()
N = len(S)
ans = [0]*N

cnt = 0
for i in range(N-1):
    if S[i] == 'R':
        cnt += 1
        if S[i+1] == 'L':
            ans[i+1] = cnt//2
            ans[i] = (cnt+1)//2
    else:
        cnt = 0


cnt = 0
for i in reversed(range(1, N)):
    if S[i] == 'L':
        cnt += 1
        if S[i-1] == 'R':
            ans[i-1] += cnt//2
            ans[i] += (cnt+1)//2
    else:
        cnt = 0

print(*ans)
