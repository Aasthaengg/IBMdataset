K = int(input())

first_mod = 7 % K
"""
cnt = 1
if first_mod == 0:
    print(1)
else:
    flg = True
    for i in range(2,K):
        seven = old * 10 + 7
        mod = seven % K
        cnt += 1
        old = seven
        if mod == 0:
            break
        if mod == first_mod:
            flg = False
            break
    if flg:
        print(cnt)
    else:
        print(-1)
"""
old_mod = now_mod = first_mod

cnt = 1
if first_mod == 0:
    print(1)
else:
    flg = False
    for i in range(2,K+1):
        now_mod = ((old_mod * 10) + 7) % K
        cnt += 1
        old_mod = now_mod
        if now_mod == 0:
            flg = True
            break
        if now_mod == first_mod:
            break
    if flg:
        print(cnt)
    else:
        print(-1)