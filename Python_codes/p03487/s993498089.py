n = int(input())
s = list(map(int,input().split()))

ans = 0
c = {}
for i in s:
    if i not in c:
        c[i] = 1
    elif c[i] < i:
        c[i] += 1
    else:
        ans += 1

for k,v in c.items():
    if k != v:
        ans += v
print(ans)
