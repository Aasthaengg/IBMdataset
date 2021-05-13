N,A,B,C = map(int,input().split())
l = [int(input()) for _ in range(N)]
ans = float('inf')
for i in range(2**N):
    da = [True]*N
    for j in range(N):
        if (i>>j) & 1:
            da[j] = False
    a = []
    lb = []
    for j in range(N):
        if da[j] == True:
            a.append(l[j])
        else:
            lb.append(l[j])
    #print(a,lb)
    if len(lb) >= 2:
        for j in range(2**len(lb)):
            db = [True] * len(lb)
            for k in range(len(lb)):
                if (j>>k) & 1:
                    db[k] = False
            b = []
            lc = []
            for k in range(len(lb)):
                if db[k] == True:
                    b.append(lb[k])
                else:
                    lc.append(lb[k])
            #print(db)
            if len(lc) >= 1:
                for k in range(2**len(lc)):
                    dc = [True] * len(lc)
                    for m in range(len(lc)):
                        if (k>>m) & 1:
                            dc[m] = False
                    c = []
                    for m in range(len(lc)):
                        if dc[m] == True:
                            c.append(lc[m])
                    if len(a) > 0 and len(b) > 0 and len(c) > 0:
                        #print(a,b,c)
                        ans = min(ans, 10*(len(a)-1)+abs(A-sum(a)) + 10*(len(b)-1)+abs(B-sum(b)) + 10*(len(c)-1)+abs(C-sum(c))          )
print(ans)


    
