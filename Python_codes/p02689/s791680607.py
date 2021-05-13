n, m = map(int,input().split())

h = list(map(int,input().split()))

mj = []

for i in range(m):
    mj.append(list(map(int,input().split())))

cnt_w = [0 for _ in range(n)]
cnt = [0 for _ in range(n)]

for i in range(m):
    cnt[mj[i][0]-1] += 1
    cnt[mj[i][1]-1] += 1
    if h[mj[i][0]-1] > h[mj[i][1]-1]:
        cnt_w[mj[i][0]-1] += 1
    elif h[mj[i][0]-1] < h[mj[i][1]-1]:
        cnt_w[mj[i][1]-1] += 1

tower = 0
for i in range(n):
    if cnt[i] == cnt_w[i]:
        tower += 1
print(tower)

