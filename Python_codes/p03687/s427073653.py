from collections import Counter

S = input()

cnt = Counter(S).most_common()

#print(cnt)

cand = [chr(i) for i in range(97, 97+26)]

anss = float('inf')
for c in cand:
    alp = c
    ans = 0
    tmp = 0
    for s in S:
        if s == alp:
            ans = max(ans, tmp)
            tmp = 0
        else:
            tmp += 1
    if tmp:
        ans = max(ans, tmp)
    anss = min(anss, ans)
print(anss)