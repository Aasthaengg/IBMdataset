from collections import Counter
n = int(input())
a_li = list(map(int,input().split()))
a_counter = Counter(a_li)
a_most = a_counter.most_common()
ans = 0
for s in a_most:
    dum = s[1] - s[0]
    if dum < 0:
        ans += s[1]
    elif dum > 0:
        ans += dum
print(ans)