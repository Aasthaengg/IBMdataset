n,k = map(int,input().split())
p = list(map(int,input().split()))
c = list(map(int,input().split()))
p = [i-1 for i in p]


groups = []
is_appear = [False]*n
group_size = [0]*n
for i in range(n):
    if is_appear[i]:
        continue
    group = []
    group.append(i)
    is_appear[i] = True
    j = p[i]
    while j != i:
        group.append(j)
        is_appear[j] = True
        j = p[j]
        
    groups.append(group)
    
    for i in group:
        group_size[i] = len(group)


cycle_score = [0]*n
for g in groups:
    score = 0
    for i in range(len(g)):
        score += c[g[i]]
    
    for i in g:
        cycle_score[i] = score

best = -float('inf')        
for i in range(n):
    score = 0
    best_i = -float('inf')
    cyc_num = k//group_size[i]
    if cycle_score[i]>0 and cyc_num>=1:
        remain = k-group_size[i]*(cyc_num-1)
        score += cycle_score[i]*(cyc_num-1)
        
    elif cycle_score[i]<=0:
        remain = group_size[i]
    elif cyc_num<1:
        remain = k
    
    j = i
    for _ in range(remain):
        j = p[j]
        score += c[j]
        best_i = max(best_i,score)
    best = max(best,best_i)
    
print(best)