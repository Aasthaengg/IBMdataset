n, m = map(int,input().split())
h = list(map(int,input().split()))

ab = [list(map(int,input().split())) for _ in range(m)]


point = [0]*n
app = [0]*n
cnt = []

for i in ab:
    app[i[0]-1] += 1
    app[i[1]-1] += 1
    if h[i[0]-1] > h[i[1]-1]:
        point[i[0]-1] += 1
    elif h[i[0]-1] < h[i[1]-1]:
        point[i[1]-1] += 1
for i in range(n):
    if app[i] == point[i]:
        cnt.append(i+1)
print(len(cnt))
