#138_E
from bisect import bisect_left, bisect_right
#leftはある数未満,rightはある数以下を返す
s = input()
t = input()
if set(s) >= set(t):
    al_idx = [[] for _ in range(26)]
    ss = s * 2
    alp = 'abcdefghijklmnopqrstuvwxyz'
    for i in range(len(ss)):
        al_idx[alp.index(ss[i])].append(i)
    
    tmp = -1
    ans = 0
    for j in range(len(t)):
        idx = alp.index(t[j])
        cur = bisect_right(al_idx[idx], tmp)
        ans += al_idx[idx][cur] - tmp
        tmp = al_idx[idx][cur] % len(s)
        
    print(ans)
else:
    print(-1)