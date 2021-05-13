import copy
s = list(input())

anslst = []
lst = copy.deepcopy(s)

for x in lst:
    ss = copy.deepcopy(s)
    n = len(ss)
    cnt = 0
    while True:
        tmp = ss[0]
        flg = 0
        for moji in ss:
            if moji != tmp:
                flg = 1
        if flg == 0:
            anslst.append(cnt)
            break

        for i in range(1, n):
            if ss[i - 1] == x or ss[i] == x:
                ss[i - 1] = x
        ss.pop()
        n = len(ss)
        cnt += 1
print(min(anslst))