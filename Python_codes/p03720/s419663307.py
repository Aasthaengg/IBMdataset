n, m = map(int, input().split())
ab = [ list(map(int, input().split())) for _ in range(m) ]
import numpy as np
ans = np.array([ [0] * n ] * n)

for i in ab:
    ans[i[0]-1][i[1]-1] += 1
    ans[i[1]-1][i[0]-1] += 1
for  i in ans:
    print(sum(i))  