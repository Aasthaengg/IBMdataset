n = int(input())
xy = [list(map(int,input().split())) for _ in range(n)]
a = []
b = []
for i in range(n):
    a.append(xy[i][0]+xy[i][1])
    b.append(xy[i][0]-xy[i][1])
a_sort = sorted(a)
b_sort = sorted(b)

print(max(a_sort[-1]-a_sort[0],b_sort[-1]-b_sort[0]))