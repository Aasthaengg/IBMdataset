d,g = map(int,input().split())
p = [0] * d
c = [0] * d
for i in range(d):
    p[i],c[i] = map(int,input().split())
ans_num = float('inf')
for i in range(2 ** d):
    score_li = list(range(1,d+1))
    ans_li = []
    ans_n = 0
    for j in range(d):
        if i >> j & 1:
            ans_li.append(p[j]*score_li[j]*100+c[j])
            score_li[j] = -1
            ans_n += p[j]
    if sum(ans_li) < g:
        s = sum(ans_li)
        score_li.sort(reverse=True)
        for k in score_li:
            for l in range(p[k-1]):
                s += k*100
                ans_n += 1
                if s >= g:
                    ans_num = min(ans_n, ans_num)
    else:
        ans_num = min(ans_n, ans_num)
print(ans_num)