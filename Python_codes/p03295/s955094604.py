import numpy as np

n,m = map(int,input().split())
arr = np.array([list(map(int,input().split())) for i in range(m)])
arr = arr[ arr[:,1].argsort(), :] #各行の1列目だけみて、行インデックスをソート
A = arr.T[0]
B = arr.T[1]

ans = 0
start,end = 0,0
for a,b in zip(A,B):
    if a < end: continue
    start,end = a,b
    ans += 1

print(ans)


