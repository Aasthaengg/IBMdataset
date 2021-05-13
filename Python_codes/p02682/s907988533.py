a,b,c,k = map(int, input().split())
s = 0
if k <= a:
    s += k
else:
    s += a
if 0 < k-(a+b):
    s -= k-(a+b)
print(s)