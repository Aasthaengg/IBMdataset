h, w = map(int, input().split())
a = [list(input()) for _ in range(h)]
dic = {}
for i in range(h):
    for j in range(w):
        if a[i][j] not in dic.keys():
            dic[a[i][j]] = 1
        else:
            dic[a[i][j]] += 1
group = {0:0, 1:0, 2:0, 3:0}
for v in dic.values():
    group[v%4] += 1
ans = 'Yes'
if group[1] + group[3] >= 2:
    ans = 'No'
else:
    if h&1 and w&1:
        if group[2] + group[3] > h//2 + w//2:
            ans = 'No'
    elif h&1 or w&1:
        if group[1] or group[3]:
            ans = 'No'
        elif group[2] > (h*w - ((h//2)*(w//2)*4))//2:
            ans = 'No'
    else:
        if group[1] or group[2] or group[3]:
            ans = 'No'
print(ans)