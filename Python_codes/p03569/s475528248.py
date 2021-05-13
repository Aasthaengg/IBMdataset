s = input()
s_ = s.replace('x', '')
if s_ != s_[::-1]:
    print(-1)
    exit()
else:
    cnt = 0
    num = 0
    for i, a in enumerate(s):
        if i + cnt >= len(s)-1:
            break
        if a == s[-1-cnt]:
            cnt += 1
            continue
        if a == 'x':
            num += 1
            continue
        else:
            while s[-1-cnt] == 'x':
                cnt += 1
                num += 1
            if a == s[-1 - cnt]:
                cnt += 1
                continue

    print(num)