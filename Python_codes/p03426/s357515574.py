h,w,d = map(int,input().split())
a = [list(map(int,input().split())) for _ in range(h)]
dic = {}
q = int(input())

for i in range(h):
    for j in range(w):
        dic[a[i][j]] = i,j

li = [0]*(h*w+1)

for i in range(d+1,h*w+1):
    if i-d not in dic:
        continue
    li[i] = li[i-d] + abs(dic[i][0]-dic[i-d][0]) + abs(dic[i][1]-dic[i-d][1])

for _ in range(q):
    l,r = map(int,input().split())
    print(li[r]-li[l])