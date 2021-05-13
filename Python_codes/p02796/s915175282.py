n = int(input())
lst = []
for i in range(n):
    x,l = map(int,input().split())
    if x-l < 0:
        # [右端の位置,左端の位置]
        lst.append([x+l,0])
    else:
        lst.append([x+l,x-l])
lst.sort()


# 最初のロボットの選択
now = lst[0][0]
cnt = 1


for i in range(1,n):
    if now <= lst[i][1]:
        now = lst[i][0]
        cnt += 1

print(cnt)