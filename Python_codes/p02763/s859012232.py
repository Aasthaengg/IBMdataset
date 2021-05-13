import sys
import bisect
import copy

N = int(sys.stdin.readline().rstrip())
S = list(sys.stdin.readline().rstrip())
Q = int(sys.stdin.readline().rstrip())

cnt = [0] * 26
cumcnt = [cnt]

for i, s in enumerate(S):
    tmp = copy.copy(cumcnt[i])
    tmp[ord(s) - ord("a")] += 1
    cumcnt.append(tmp)

q_remove = {}
q_add = {}

for _ in range(Q):
    t, i, c = sys.stdin.readline().rstrip().split()
    t = int(t)
    i = int(i)
    d = S[i - 1]
    if t == 1:
        if d != c:
            if d not in q_remove.keys():
                q_remove[d] = [i]
            else:
                bisect.insort(q_remove[d], i)
            if c not in q_add.keys():
                q_add[c] = [i]
            else:
                bisect.insort(q_add[c], i)
            S[i - 1] = c 
    else:
        c = int(c)
        cnt_l = copy.copy(cumcnt[i - 1])
        cnt_r = copy.copy(cumcnt[c])
        for q, idx in q_add.items():
            x = bisect.bisect_right(idx, i - 1)
            y = bisect.bisect_right(idx, c)
            cnt_l[ord(q) - ord("a")] += x
            cnt_r[ord(q) - ord("a")] += y
        for q, idx in q_remove.items():
            x = bisect.bisect_right(idx, i - 1)
            y = bisect.bisect_right(idx, c)
            cnt_l[ord(q) - ord("a")] -= x
            cnt_r[ord(q) - ord("a")] -= y
        ans = 0
        for l, r in zip(cnt_l, cnt_r):
            if r - l > 0:
                ans += 1
        print(ans)