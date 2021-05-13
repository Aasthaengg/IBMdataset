from collections import Counter
s = input()
k = int(input())

# 全部同じ
C = Counter(s)
if len(C) == 1:
    print(len(s) * k // 2)
    exit()

# 両端が異なる
if s[0] != s[-1]:
    aida = 0
    cnt = 0
    for i in range(1,len(s)):
        if s[i] == s[i-1]:
            cnt += 1
        else:
            tmp = cnt // 2
            if cnt % 2 != 0:
                aida += tmp + 1
            else:
                aida += tmp
            cnt = 0
    tmp = cnt // 2
    if cnt % 2 != 0:
        aida += tmp + 1
    else:
        aida += tmp


    print(aida * k)

# 両端が同じ
else:
    # 先端の個数
    cnt = 1
    for i in range(1,len(s)):
        if s[i] == s[i-1]:
            cnt += 1
        else:
            break
    # 末端の個数
    cnt2 = 1
    for i in range(len(s)-1,-1,-1):
        if s[i] == s[i-1]:
            cnt2 += 1
        else:
            break

    # 先端で書き換える個数
    syoko = cnt // 2

    # 末端＋先端で書き換える個数
    sotogawa = (cnt + cnt2) // 2

    # 先端と末端の間で書き換える個数
    aida = 0
    cnt3 = 0
    #print(s[cnt : len(s)-cnt2])
    for i in range(cnt+1,len(s)-cnt2+1):
        if s[i] == s[i-1]:
            cnt3 += 1
        else:
            tmp = cnt3 // 2
            if cnt3 % 2 != 0:
                aida += tmp + 1
            else:
                aida += tmp
            cnt3 = 0

    saikuru = aida + sotogawa
    print(syoko + saikuru * k - saikuru + aida + cnt2//2)




