N,*s = open(0).read().split()
ans = sum(x.count('AB') for x in s)
bxa, xa, bx = 0, 0, 0
for x in s:
    if x[0] == 'B':
        if x[-1] == 'A':
            bxa += 1
        else:
            bx += 1
    elif x[-1] == 'A':
        xa += 1
if bxa > 0:
    ans += bxa - 1
    if xa > 0:
        ans += 1
        xa -= 1
    if bx > 0:
        ans += 1
        bx -= 1
    ans += min(xa,bx)
else:
    ans += min(xa,bx)
print(ans)