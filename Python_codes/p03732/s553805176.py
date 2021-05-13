n, max_w = map(int, input().split())
item = [tuple(int(x) for x in input().split()) for _ in range(n)]

ans = dict()
ans[0] = 0
for w, v in item:
    next = dict()
    for temp_w, temp_v in ans.items():
        if temp_w + w <= max_w:
            if temp_w + w not in next.keys():
                next[temp_w + w] = temp_v + v
            else:
                if temp_v + v > next[temp_w + w]:
                    next[temp_w + w] = temp_v + v
    #print(next)
    for x, y in next.items():
        if x not in ans.keys():
            ans[x] = y
        else:
            if y > ans[x]:
                ans[x] = y

#print(ans)
res = 0
for x, y in ans.items():
    res = max(res, y)

print(res)
