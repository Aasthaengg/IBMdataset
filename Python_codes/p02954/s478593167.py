S = input()

# 一人ずつ場所を確定させる
# 進行方向に見ていって反対方向のシンボルが現れたら停留点はその場所のLRのどちらか偶奇で判断

import bisect

l = []
x = 0
for s1, s2 in zip(S[0] + S, S):
    if s1 != s2:
        x += 1
    l.append(x)

ans = [0] * len(S)
for i in range(len(S)):
    if S[i] == 'R':
        target = bisect.bisect_left(l, l[i]+1, lo=i)
    else:
        target = bisect.bisect_right(l, l[i]-1, hi=i) - 1
    
    # 余りが出れば、targetがLなら+1、Rなら-1
    diff = abs(target - i)
    if diff % 2 == 1:
        if S[i] == 'R':
            target -= 1
        else:
            target += 1
    
    ans[target] += 1

print(*ans)