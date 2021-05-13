#41 A - Shrinking
import collections 
s = list(input())
cnt = collections.Counter(s)
valcnt = list(cnt.values())
M = max(valcnt)
# 出現回数が最多の文字リスト
mkeys = [i for i,v in cnt.items() if v == M]

ans = len(s)
for key in s:
    m = 0
    cnt = 0
    # 最多の文字の区間の最大値がその文字の最小値
    for S in s:
        if S == key: 
            m = max(m,cnt)
            cnt = 0
        else:
            cnt += 1
    m = max(m,cnt)
    ans = min(ans,m)

print(ans)