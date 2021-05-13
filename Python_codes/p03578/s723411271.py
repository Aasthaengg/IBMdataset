from collections import Counter
n = int(input())
d = list(map(int,input().split()))
m = int(input())
t = list(map(int,input().split()))
d = Counter(d)
t = Counter(t)
f = 1
for a,b in t.items():
    if d[a] < b:
        f = 0
        break
print("YES" if f else "NO")