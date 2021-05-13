import collections
n = int(input())
d = list(map(int, input().split()))
m = int(input())
t = list(map(int, input().split()))

d = dict(collections.Counter(d))
t = dict(collections.Counter(t))

for k, v in t.items():
    if d.get(k, 0) < v:
        print("NO")
        exit()
else:
    print("YES")
