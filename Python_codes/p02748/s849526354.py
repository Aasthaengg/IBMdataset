a,b,m = map(int,input().split())
a_list = list(map(int,input().split()))
b_list = list(map(int,input().split()))
xyc = [list(map(int,input().split())) for _ in range(m)]
a_min = min(a_list)
b_min = min(b_list)
s = a_min + b_min
for i in range(m):
    x,y,c = xyc[i][0]-1,xyc[i][1]-1,xyc[i][2]
    s = min(s, a_list[x]+b_list[y]-c)
print(s)