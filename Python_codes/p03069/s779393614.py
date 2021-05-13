N = int(input())
S = input()

tmp = 10 ** 9
cntB = S.count("#")
cnt = 0
for i, s in enumerate(S):
    if s == "#":
        tmp = min(tmp, cnt + N - i - (cntB - cnt))
        cnt += 1

print(min(cntB, tmp))
