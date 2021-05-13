n, x = [int(w) for w in input().split()]
a_li = [int(w) for w in input().split()]
a_li.sort()
 
ans = 0
for a in a_li:
    x -= a
    if x >= 0:
        ans += 1
    else:
        break
 
if x == 0:
    pass
else:
    if x > 0:
        ans = max(ans - 1, 0)
 
print(ans)