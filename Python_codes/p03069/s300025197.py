N = int(input())
S = list(input())
data = [0] * (N + 2)
cnt = 0
for i in range(N):
    if S[i] == "#":
        cnt += 1
    data[i + 1] = cnt
data[-1] = cnt
ans = float("inf")
for i in range(N + 1):
    turn = data[i] + N - i - data[-1] + data[i]
    if ans > turn:
        ans = turn
print(ans)