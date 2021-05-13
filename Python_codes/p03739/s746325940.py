n = int(input())
a = list(map(int, input().split()))
ans1, ans2 = 0, 0
cnt1, cnt2 = 0, 0
cur = 1
for i in a:
    cnt1 += i
    if cnt1 * cur <= 0:
        ans1 += abs(cnt1 - cur)
        cnt1 = cur
    cur *= -1
cur = -1
for i in a:
    cnt2 += i
    if cnt2 * cur <= 0:
        ans2 += abs(cnt2 - cur)
        cnt2 = cur
    cur *= -1
print(min(ans1, ans2))