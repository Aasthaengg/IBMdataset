N = int(input())
if N == 1:
    st = 0
    S = input()
    for x in S:
        if x == '(':
            st += 1
        else:
            if st > 0:
                st -= 1
            else:
                print('No')
                exit()
    if st == 0:
        print('Yes')
    else:
        print('No')
    exit()
lst1, lst2 = [], []
flg, mr = 0, 10**9
for i in range(N):
    S = input()
    st, r, rall = 0, 0, 0
    for c in S:
        if c == '(':
            st += 1
        else:
            rall += 1
            if st > 0:
                st -= 1
            else:
                r += 1
    pls = max(0, len(S)-rall-(rall-r))
    if pls >= r:
        lst1.append((r, -pls))
    else:
        lst2.append((-pls, r))
lst1.sort()
lst2.sort()
if lst1[0][0] != 0:
    print('No')
    exit()
lcnt = -lst1[0][1]
for (r, pls) in lst1[1:]:
    lcnt -= r
    if lcnt < 0:
        print('No')
        exit()
    lcnt -= pls
for (pls, r) in lst2:
    lcnt -= r
    if lcnt < 0:
        print('No')
        exit()
    lcnt -= pls
if lcnt == 0:
    print('Yes')
else:
    print('No')