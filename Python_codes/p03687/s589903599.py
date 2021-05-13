from collections import Counter
s = list(input())
d =  Counter(s)
key = d.keys()
ans = len(s)//2 + len(s)%2
for k in key:
    ck = 0
    i = 0
    while True:
        if s[i] == k:
            i += 1
            if i == len(s):
                break
        else:
            cnt = 0
            while s[i + cnt] != k:
                cnt += 1
                if i + cnt == len(s):
                    break
            ck = max(ck, cnt)
            i += cnt
            if i == len(s):
                break
    ans = min(ans, ck)
print(ans)