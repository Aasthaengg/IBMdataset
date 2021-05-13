x,n = map(int, input().split())
p = list(map(int, input().split()))
y1 = x
y2 = x
while y1 > 0 and y2 <= 100:
    if y1 in p:
        y1 += 1
    else: break
    if y2 in p:
        y2 -= 1
    else: break
ans = [100,100]
if y1 not in p:
    ans[0] = abs(x-y1)
if y2 not in p:
    ans[1] = abs(x-y2)
print(y2 if min(ans) == ans[1] else y1)