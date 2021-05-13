import numpy as np

n,m = map(int,input().split())
arr = np.array([list(map(int,input().split())) for i in range(m)])
arr = arr[ arr[:,1].argsort(), :] #各行の1列目だけみて、行インデックスをソート


ans = 0
start,end = 0,0
for ab in arr:
    a,b = ab[0],ab[1]
    if a < end: continue
    start,end = a,b
    ans += 1

print(ans)


