# AtCoder
N, K = map(int, input().split())
R, S, P = map(int, input().split())
T = input()

ans = []
for i in range(N):
    if T[i] == 's':
        ans.append('r')
    elif T[i] == 'r':
        ans.append('p')
    elif T[i] == 'p':
        ans.append('s')

    if i >= K:
        if ans[i-K] == ans[i]:
            ans[i] = ''

count = 0
for i in range(N):
    # あいこ処理　
    if (T[i] == ans[i]) or ('' == ans[i]):
        continue

    if ans[i] == 'r':
        count += R
    elif ans[i] == 's':
        count += S
    elif ans[i] == 'p':
        count += P

print(count)
