from itertools import accumulate

N = int(input())
As = list(map(int, input().split()))
acc = list(accumulate(As))

# 偶数が正
ans = 0
cnt = 0 #累積カウント
parity = [1,-1]
for i,a in enumerate(acc):
    a += cnt
    p = parity[i%2]
    if p * a > 0:
        continue
    else:
        ans += abs(a)+1
        cnt += p*(abs(a)+1)

# 偶数が負
ans2 = 0
cnt = 0 #累積カウント
parity = [-1,1]
for i,a in enumerate(acc):
    a += cnt
    p = parity[i%2]
    if p * a > 0:
        continue
    else:
        ans2 += abs(a)+1
        cnt += p*(abs(a)+1)

print(min(ans,ans2))
