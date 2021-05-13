n = int(input().rstrip())
aa = list(map(int, input().split()))
bb = list(map(int, input().split()))

ans = 0
resid = 0
for i in range(n):
    prev_beat = min(resid, aa[i])
    cur_beat = min(aa[i] - prev_beat, bb[i])
    ans += prev_beat
    ans += cur_beat
    resid = bb[i] - cur_beat
ans += min(resid, aa[n])

print(ans)