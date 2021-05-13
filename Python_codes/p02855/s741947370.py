h, w, k = map(int,input().split())
S = [[] for _ in range(h)]
ans = [[0]*w for _ in range(h)]

for i in range(h):
    S[i] = list(input())

base = 1
for hi in range(h):
    if '#' in S[hi]:
        t = False
        for wi in range(w):
            if S[hi][wi]=='#':
                if t:
                    for wii in range(wi):
                        ans[hi][wii] += 1
                else:
                    t = True
                    for wii in range(w): ans[hi][wii] = base
        base = max(max(ans))+1

for wi in range(w):
    chi = [ans[hi][wi] for hi in range(h) if ans[hi][wi]!=0]
    nowchi = 0
    for hi in range(h):
        if ans[hi][wi]==0:
            ans[hi][wi] = chi[nowchi]
        elif ans[hi][wi]==chi[nowchi] and nowchi<len(chi)-1:
            nowchi += 1

for _ans in ans:
    print(*_ans)