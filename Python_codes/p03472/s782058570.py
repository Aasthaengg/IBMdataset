n, h = map(int,input().split())
a = []
b = []
ans = 0

for i in range(n):
    x, y = map(int,input().split())
    a.append(x)
    b.append(y)

b.sort(reverse=True)
c = max(a)

#刀を投げる
for i in b:
    if i > c:
        h -= i
        ans += 1
        if h <= 0:
            print(ans)
            exit()

#刀を振る
ans += (h+c-1)//c
print(ans)