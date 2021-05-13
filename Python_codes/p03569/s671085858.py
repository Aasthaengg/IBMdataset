s = str(input())
ns = s.replace('x', '')
l = len(ns)
if l == 0:
    print(0)
elif l == 1:
    idx = s.find(ns)
    print(abs(idx - (len(s) - idx - 1)))
else:
    cnt = 0
    L = []
    for i in range(l // 2):
        if ns[i] != ns[-(i+1)]:
            print(-1)
            break
        else:
            L.append(ns[i])
    else:
        if l % 2:
            L.append(ns[i+1])
        pleft = 0
        pright = 0
        for c in L:
            if pleft == 0:
                left = s.find(c)
            else:
                left = s[pleft:].find(c)
            if pright == 0:
                right = len(s) - s.rfind(c) - 1
            else:
                right = len(s) - (s[:-pright].rfind(c) + pright + 1)
            pleft = left + pleft + 1
            pright = right + pright + 1
            cnt += abs(left - right)
        print(cnt)
