S = input()
N = len(S)
ans = [0] * N
c = 0
for i in range(N):
    if S[i] == 'R':
        c += 1
    else:
        ans[i] += c // 2
        ans[i - 1] += c // 2 + c % 2
        c = 0
for i in range(N - 1, -1, -1):
    if S[i] == 'L':
        c += 1
    else:
        ans[i] += c // 2
        ans[i + 1] += c // 2 + c % 2
        c = 0
print(*ans)
