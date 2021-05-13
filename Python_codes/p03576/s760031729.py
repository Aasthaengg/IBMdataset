n, k =  [ int(v) for v in input().split() ] 
node_list = [] 
x_list = []
y_list = []

for i in range(n):
    x, y = [ int(v) for v in input().split() ]
    node_list.append((x,y))
    x_list.append(x)
    y_list.append(y)
x_list.sort()
y_list.sort()


x_list = [ (x_list[i],x_list[j]) for i in range(n-k+1) for j in range(i+k-1,n) ]
y_list = [ (y_list[i],y_list[j]) for i in range(n-k+1) for j in range(i+k-1,n) ]

def check(in_x,in_y):
    xl, xr, yu, yd = in_x[0], in_x[1], in_y[0], in_y[1]
    ok = 0
    for i in node_list:
        if xl <= i[0] <= xr and yu <= i[1] <= yd:
            ok += 1

    if ok >= k:
        return (xr-xl) * (yd-yu)
    else:
        return 10**19

ans = 10**19
for i in x_list:
    for j in y_list:
        ans = min(ans, check(i,j))
print(ans)
