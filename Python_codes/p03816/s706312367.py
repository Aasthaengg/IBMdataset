from collections import Counter

x = int(input())
a = list(map(int,input().split()))
c = Counter(a)
t = c.most_common()
d = 0
l = len(set(a))
for i in range(l):
    if t[i][1]>1:
        d+=t[i][1]-1
ans = l-d%2
print(ans)
