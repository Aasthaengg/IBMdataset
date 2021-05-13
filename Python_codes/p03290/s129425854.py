D, G = map(int, input().split())
p = [0] * D
c = [0] * D
for i in range(D):
    p[i], c[i] = map(int, input().split())
    
cnt_min = sum(p)

for i in range(2**D):
    flg = [False] * D
    cnt = 0
    score = 0
    for j in range(D):
        if i & (1 << D-1-j):
            flg[j] = True
            cnt += p[j]
            score += p[j]*(j+1)*100 + c[j]
    
    if score >= G:
        if cnt < cnt_min:
            cnt_min = cnt
    else:
        for j in reversed(range(D)):
            if flg[j]:
                continue
            for k in range(p[j]-1):
                cnt += 1
                score += (j+1)*100
                if score >= G:
                    if cnt < cnt_min:
                        cnt_min = cnt
                        break                        
            break
print(cnt_min)