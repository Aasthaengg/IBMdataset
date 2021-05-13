N, M = map(int, input().split())
ac = 0
is_AC = [False] * (N + 1)
WA_cnt = [0] * (N + 1)
for i in range(M):
    p, s = input().split()
    p = int(p)
    if s == 'WA':
        if is_AC[p]:
            continue
        else:
            WA_cnt[p] += 1
    else:
        if is_AC[p]:
            continue
        else:
            is_AC[p] = True
            ac += 1

wa = 0
for i in range(N + 1):
    if is_AC[i]:
        wa += WA_cnt[i]
print(ac, wa)
'''
うまくいかなかったパターン
1 4
1 WA
1 WA
1 WA
1 WA
'''
