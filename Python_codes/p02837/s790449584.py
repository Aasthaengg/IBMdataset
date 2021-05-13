n = int(input())

s = [[] for _ in range(n)]
for i in range(n):
    a = int(input())
    for _ in range(a):
        x, y = map(int,input().split())
        s[i].append((x-1, y))

ans = 0
for state in range(1<<n):
    tmp = 0
    hh = []
    for mask in range(n):
        if (1<<mask)&state:
            hh.append(mask)
    flag = True
    for h in hh:
        for x,y in s[h]:
            if y == 1:
                if x not in hh:
                    flag = False
                    break
            else:
                if x in hh:
                    flag = False
                    break
        tmp += 1
    if flag:        
        ans = max(tmp, ans)
    
print(ans)