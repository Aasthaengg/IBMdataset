from collections import Counter

s = input()
s_len = len(s)
c = Counter(s)
ans = float('inf')
for k in c.keys():
    tmp = list(s)
    cnt = 0
    while True:
        if len(set(tmp)) == 1:
            break
        for i in range(len(tmp)-1):
            if tmp[i] == k:
                tmp[i] = k
            elif tmp[i+1] == k:
                tmp[i] = k
            else:
                continue
        else:
            tmp = tmp[:-1]
            cnt += 1
    ans = min(ans,cnt)
print(ans)