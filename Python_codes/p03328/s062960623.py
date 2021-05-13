a, b = map(int, input().split())
snow = b - a
h = []
tmp = 0
for i in range(1,1000):
    tmp += i
    h.append(tmp)
x =[h[j+1] - h[j] for j in range(998)]
y = x.index(snow)
print(h[y] - a)