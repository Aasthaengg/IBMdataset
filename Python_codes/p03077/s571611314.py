n = int(input())
a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())
x = min(a, b, c, d, e)
ans = 4 + n//x
if n%x != 0:
    ans += 1
print(ans)