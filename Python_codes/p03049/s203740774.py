n = int(input())
cnt_AB = 0
cnt_xxA = 0
cnt_Bxx = 0
cnt_BxA = 0
for i in range(n):
    s = input()
    cnt_AB += s.count('AB')
    if s[-1] == 'A' and s[0] != 'B':
        cnt_xxA += 1
    if s[0] == 'B' and s[-1] != 'A':
        cnt_Bxx += 1
    if s[-1] == 'A' and s[0] == 'B':
        cnt_BxA += 1

if cnt_BxA == 0:
    print(cnt_AB + min(cnt_xxA, cnt_Bxx))
else:
    if cnt_Bxx+cnt_xxA > 0:
        print(cnt_AB + cnt_BxA + min(cnt_xxA, cnt_Bxx))
    else:
        print(cnt_AB + cnt_BxA - 1)