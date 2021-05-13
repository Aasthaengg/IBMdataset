a = int(input())
b = int(input())
c = int(input())
d = int(input())

ans = 0
if a >= b:
    ans += b
elif b > a:
    ans += a
    
if c >= d:
    ans += d
elif d > c:
    ans += c
    
print(ans)