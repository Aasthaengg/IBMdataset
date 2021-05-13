n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
ans = 0
d = []
s = 0
for ai, bi in zip(a, b):
    if ai < bi:
        ans += 1
        s += bi - ai
    else:
        d.append(ai - bi)
if ans:
    d.sort(reverse=True)
    ds = 0
    for di in d:
        ds+=di
        ans+=1
        if ds >= s:
            break
    if ds < s:
        print(-1)
    else:
        print(ans)
else:
    print(0)
