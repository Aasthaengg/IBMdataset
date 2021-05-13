n = int(input())
S = input()
#右にある白，左にある黒
cnt = [0]*(n+1)
white = S.count(".")
black = 0
cnt[0] = white
for i in range(n):
    if S[i] == ".":
        white -= 1
    else:
        black += 1
    cnt[i+1] = black + white
print(min(cnt))