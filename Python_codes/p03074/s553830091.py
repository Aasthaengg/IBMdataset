N, K = map(int, input().split())
S = list(input())

ttl = []
prev = S[0] # 0
cnt = 1
if S[0] == '0':
    ttl.append(0)
for i in range(1, N):
    if S[i] == prev:
        cnt += 1
    else:
        ttl.append(cnt)
        cnt = 1
    prev = S[i]
if cnt != 0:
    ttl.append(cnt)
if S[-1] == '0':
    ttl.append(0)
l = len(ttl)
sums = [0] * (l + 1)
for i in range(l):
    sums[i+1] = sums[i] + ttl[i]

cnt_width = 2 * K + 1
ans = 0
chk_l = len(sums)
for left in range(0, chk_l, 2):
    right = left + cnt_width
    if right >= chk_l:
        right = chk_l - 1
    ans = max(ans, sums[right] - sums[left])
    if left >= chk_l - 1 - cnt_width:
        break
print(ans)