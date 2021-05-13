n = int(input())
if n == 1:
    print(1)
else:
    buf = []
    for i in range(n):
        x,y = map(int,input().split())
        buf.append([x,y])
    
    buf.sort()
    
    ans = 1e9
    for i in range(n):
        for j in range(i+1,n):
            p,q = buf[j][0]-buf[i][0],buf[j][1]-buf[i][1]
    
            ind = 0
            used = set()
            tcost = 0
            befx = 0
            befy = 0
            flag = False
            while True:
                befx,befy = buf[ind][0],buf[ind][1]
                tcost += 1
                for l in range(n):
                    if l not in used:
                        tx,ty = buf[l][0],buf[l][1]
                        if tx-befx == p and ty-befy == q:
                            befx = tx
                            befy = ty
                            used.add(l)
                while True:
                    ind += 1
                    if ind == n:
                        flag = True
                        break
                    if ind in used:
                        continue
                    else:
                        break
                if flag:
                    break
            if ans > tcost:
                # print(used)
                # print(p,q,tcost)
                ans = tcost
    
    print(ans)



