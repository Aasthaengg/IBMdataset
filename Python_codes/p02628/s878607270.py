asdfasdfasdf, a = map(int, input().split())
b = list(map(int, input().split()))
d = 0
for c in range(a):
    d += min(b)
    b.remove(min(b))
print(d)