N,H,W = map(int,input().split())

arr = []
count = 0
for i in range(N):
    arr.append(list(map(int,input().split())))

for i in arr:
    if i[0] >= H and i[1] >= W:
        count+=1

print(count)