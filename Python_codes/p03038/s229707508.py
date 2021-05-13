n, m = map(int, input().split())
a = list(map(int, input().split()))
bc = [ list(map(int, input().split())) for _ in range(m)]


# 最小値から順にCjより小さければ書き換えればよい　
# 毎回ソートしていたら間に合わなさそう
# Cを大きい順にソートして、カードの最小値をpop, キューの最後にCを加える
from collections import deque
import numpy as np
npbc = np.array(bc)
npbc = npbc[np.argsort(npbc[:, 1])[::-1]]
bc = npbc.tolist()
# print(bc)

que = deque(sorted(a))
for b, c in bc:
    for i in range(b):
        val = que.popleft()
        if val < c:
            que.append(c)
        else:
            que.appendleft(val)
            if i == 0:
                # print(que)
                print(sum(que))
                exit()
            else:
                break

# print(que)
print(sum(que))