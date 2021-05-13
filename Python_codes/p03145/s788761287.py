a,b,c = map(int, input().split())
if a > b and a > c:print(b * c // 2)
if b > c and b > a:print(c * a // 2)
if c > a and c > b:print(a * b // 2)
