#!/usr/bin/env python3
import numpy as np
N, A, B = map(int, input().split())
X = np.array(list(map(int, input().split())))
diff = np.diff(X)
ans = 0
for d in diff:
    if d * A <= B:
        ans += d * A
    else:
        ans += B
print(ans)