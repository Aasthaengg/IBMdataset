n = int(input())
S = [str(input()) for _ in range(n)]

a = 0
b = 0
ab = 0
ans = 0
for s in S:
    ans += s.count('AB')
    if s[0] == 'B' and s[-1] == 'A':
        ab += 1
    elif s[0] == 'B':
        b += 1
    elif s[-1] == 'A':
        a += 1
    else:
        pass
if ab:
    ans += ab-1
if ab:
    if a:
        ans += 1
        a -= 1
    if b:
        ans += 1
        b -= 1
ans += min(a, b)
print(ans)
