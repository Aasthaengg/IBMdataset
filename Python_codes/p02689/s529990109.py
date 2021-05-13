n, m = map(int, input().split())
h = list(map(int, input().split()))
paths = []
for _ in range(m):
    a, b = map(int, input().split())
    if a>b:
        paths.append([b, a])
    else :
        paths.append([a, b])


ans = [True] * n
# for i in range(n):
#     ans.append(i+1)
    
for j in range(m):
    path = paths[j]
    if h[path[0]-1] > h[path[1]-1]:
        ans[path[1]-1] = False
    elif h[path[0]-1] < h[path[1]-1]:
        ans[path[0]-1] = False
    else :
        ans[path[1]-1] = False
        ans[path[0]-1] = False
        

print(ans.count(True))