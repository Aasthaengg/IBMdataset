import collections
s = list(input())
sset = set(s)
if len(sset) != 26:
    for i in range(97,123):
        if chr(i) in sset:
            continue
        else:
            tmp = chr(i)
            s.append(tmp)
            break

    print(''.join(s))
    exit()
else:
    tmp = []
    flg = False
    for i in range(1,26):
        if s[i-1] < s[i]:
            tmp.append(i-1)
            continue

    if len(tmp) == 0:
        print(-1)
        exit()
    change_i = max(tmp)
    if change_i == 0:
        print(chr(ord(s[0])+1))
        exit()
    ans = s[:change_i]
    for i in range(97,123):
        if chr(i) in ans:
            continue
        else:
            if ord(s[change_i]) < i:
                ans.append(chr(i))
                break
    print(''.join(ans))
