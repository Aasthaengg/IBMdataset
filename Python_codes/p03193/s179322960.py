N , H , W = map(int,input().split())
lst = []
for i in range(N):
    lst.append(list(map(int,input().split())))

cnt = 0
for v in lst:
    if v[0] >= H and v[1] >= W:
        cnt += 1
print(cnt)