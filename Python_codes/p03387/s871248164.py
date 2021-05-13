a,b,c = map(int,input().split())
d = max(a,b,c)
p = (d-a)+(d-b)+(d-c)
if p % 2 != 0:
    p += 3
print(p // 2)