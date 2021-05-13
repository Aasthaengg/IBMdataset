N = int(input())
S = input()

white = [0] * (N + 1)
for i in range(N):
    if S[i] == ".":
        white[i + 1] = white[i] + 1
    else:
        white[i + 1] = white[i]

ans = N
for i in range(N + 1):
    tmp = (i - white[i]) + (white[-1] - white[i])
    if tmp < ans:
        ans = tmp

print(ans)
