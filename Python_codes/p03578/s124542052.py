from collections import Counter
n = int(input())
d = list(map(int, input().split()))
m = int(input())
t = list(map(int, input().split()))
ans = "YES"
dc = Counter(d)
tc = Counter(t)
for k,v in tc.items():
    if dc[k]<v:
        ans = "NO"
print(ans)