a,b,c = map(int,input().split())
c -= a
ans = a
a = 0
ans += 2 * min(b,c)
num = min(b,c)
b -= num
c -= num
if c:
    ans += 1
else:
    ans += b
print(ans)