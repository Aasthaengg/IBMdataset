d,g = map(int,input().split())
pc = [0]*d
for i in range(d):
    pc[i] = list(map(int,input().split()))
ans_new = float("inf")
for i in range(1<<d):
    num = 0
    ans = 0
    for j in range(d):
        if (i >> j)%2 == 1:
           num += pc[j][0]*(j+1)*100 + pc[j][1]
           ans += pc[j][0]
    if num < g:
        dum = 0
        for k in range(d):
            if (i >> k)%2 == 0:
               dum = k
        for l in range(pc[dum][0]):
            num += (dum+1)*100
            ans += 1
            if num >= g:
                break
        else:
            continue
    ans_new = min(ans,ans_new)
print(ans_new)