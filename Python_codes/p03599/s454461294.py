A, B, C, D, E, F = map(int, input().split())
ans = 0
answ = A*100
anss = 0
for a in range(30//A+1):
    for b in range((30-a*A)//B+1):
        # print(a, b)
        w = (a*A + b*B) * 100
        if w > F:
            break
        elif w == 0:
            continue
        # print(a, b)
        sc = (w / 100) * E
        # print(E, sc)
        for c in range(int(sc//C)+1):
            for d in range(int((sc-c*C)//D)+1):
                s = c*C + d*D
                if s > sc or w + s > F:
                    break
                tmp = s / (w + s)
                # print(a, b, s, sc, tmp)
                if ans < tmp:
                    ans = tmp
                    answ = w
                    anss = s
print(answ+anss, anss)