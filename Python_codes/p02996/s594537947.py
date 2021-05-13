n = int(input())
d = {}
s = 0
for i in range(n):
    a, b = map(int, input().split())
    if b not in d:
        d.update({b:a})
    else:
        d[b] += a
    s += a
key = list(d.keys())
key.sort(reverse = True)
ans = True
for k in key:
    if k < s:
        ans = False
        break
    s -= d[k]
if ans:
    print("Yes")
else:
    print("No")