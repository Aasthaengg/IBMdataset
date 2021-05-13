import collections
s = input()
a = []
for i in range(26):
    cnt = collections.Counter(s)[chr(i+97)]
    if cnt == 0:
        a.append(len(s))
        continue
    num = 0
    ma = 0
    for j in s:
        if j == chr(i+97):
            ans = num
            ma = max(ma, ans)
            num = 0
        else:
            num += 1
        ans = num
        ma = max(ma, ans)
    a.append(ma)
print(min(a))