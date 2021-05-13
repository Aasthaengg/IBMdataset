import numpy as np

h,w = map(int,input().split())
n = int(input())
lst = list(map(int,input().split()))

g = []
for i in range(n):
    for _ in range(lst[i]):
        g.append(i+1)

arr = np.array(g)
arr = arr.reshape([h,w])

ans = []
for i in range(h):
    tmp = list(arr[i])
    if i%2 != 0:
        tmp.reverse()
    ans.append(tmp)

for i in range(h):
    print(*ans[i])