N = int(input())
S = input()

b, w = 0, 0
for i in range(N):
    if S[i] == '#':
        b += 1
    else:
        w += 1

ans = [0 for _ in range(N+1)]
ans[0], ans[-1] = w, b
for i in range(1, N):
    if S[i-1] == '#':
        ans[i] = ans[i-1] + 1
    else:
        ans[i] = ans[i-1] - 1

print(min(ans))