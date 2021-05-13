n, m = [int(i) for i in input().split()]
abc = []
for _ in range(m):
    a, b, c = [int(i) for i in input().split()]
    abc.append([a - 1, b - 1, c])

dist = [-10 ** 18] * n
dist[0] = 0

def update():
    global dist
    for a, b, c in abc:
        if dist[a] + c > dist[b]:
            dist[b] = dist[a] + c

for _ in range(n):
    update()
a = dist[-1]
for _ in range(n):
    update()
b = dist[-1]
if a != b:
    print("inf")
else:
    print(a)