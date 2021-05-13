S = input()
if S[0] == 'A' and S[2:-1].count('C') == 1:
    chk = S.replace('A', '').replace('C', '')
    l = len(chk)
    cnt = 0
    for s in chk:
        if s.islower():
            cnt += 1
    if cnt == l:
        print('AC')
        exit()
print('WA')