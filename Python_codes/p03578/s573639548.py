from collections import Counter
n = int(input())
d = Counter(list(map(int, input().split())))
m = int(input())
t = Counter(list(map(int, input().split())))
key = t.keys()
ans = True
for i in key:
    if t[i] > d[i]:
        ans = False
        break
if ans:
    print("YES")
else:
    print("NO")
