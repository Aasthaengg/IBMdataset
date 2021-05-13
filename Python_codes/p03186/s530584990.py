a, b, c = map(int, input().split())

ans = 0
if c <= a+b:
    ans += b+c
elif b < c:
    ans += 2*b + a+1
else:
    ans += b+c

print(ans)
