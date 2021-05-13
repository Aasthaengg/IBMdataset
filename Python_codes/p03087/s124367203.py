N, Q = map(int, input().split())
S = input()
ans = [0]*(N+1)
for i in range(N):
    ans[i+1] = ans[i]
    if S[i: i+2] == 'AC':
        ans[i+1] += 1
for _ in range(Q):
    start, end = map(int, input().split())
    cnt = ans[end-1] - ans[start-1]
    print(cnt)
