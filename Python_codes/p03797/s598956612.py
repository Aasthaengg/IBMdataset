n,m = map(int,input().split())
s = n
c = m
if 2 * s < c:
    add = (c - 2*s) // 4
    ans = s + add
elif 2 * s == c:
    ans = s
else:
    ans = c // 2
print(ans)
