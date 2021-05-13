import numpy as np
n = int(input())
l = np.array(sorted(list(map(int, input().split()))))

ans = 0
for i in range(n-1):
    ans += l[i+1] - l[i]
print(ans)
