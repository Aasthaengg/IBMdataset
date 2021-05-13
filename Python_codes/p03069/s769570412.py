from itertools import accumulate


N = int(input())
S = input()
black = [0] * N
white = [0] * N
for i in range(N):
    if S[i] == "#":
        black[i] = 1
    else:
        white[i] = 1
black = list(accumulate(black, initial=0))
white = list(accumulate(white, initial=0))
ans = float("inf")
for i in range(N + 1):
    ans = min(ans, black[i] + white[N] - white[i])
print(ans)
