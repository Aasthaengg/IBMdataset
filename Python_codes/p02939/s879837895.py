S = list(input())
N = len(S)
pre = '#'
now = ''
cnt = 0

for i in range(N):
    now += S[i]
    if now != pre:
        cnt += 1
        pre = now
        now = ''

print(cnt)