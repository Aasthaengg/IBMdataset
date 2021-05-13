ab = lambda a,b:abs(a-b)
area = lambda a,b:ab(a[1],b[1])*ab(a[0],b[0])

N, K = map(int, input().split())
A = []
x_lst = []
y_lst = []
for i in range(N):
    a,b = map(int, input().split())
    A.append([a,b])
    x_lst.append(a)
    y_lst.append(b)

x_lst.sort()
y_lst.sort()
mn = float('INF')
for x in range(N-1):
    for x_ in range(x,N):
        for y in range(N-1):
            for y_ in range(y,N):
                cnt = 0
                for a,b in A:
                    if x_lst[x] <= a <= x_lst[x_] and y_lst[y] <= b <= y_lst[y_]:
                        cnt += 1
                if cnt >= K:
                    mn = min(mn, area([x_lst[x],y_lst[y]], [x_lst[x_], y_lst[y_]]))
print(mn)
