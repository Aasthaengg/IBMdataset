import numpy as np

n = int(input())
p = np.array(list(map(int, input().split())))

comp = np.arange(n) + 1
diff = list(comp - p)

diff = [~(x == 0) for x in diff] + [True]

ans = 0
for i in range(len(diff) - 1):
    if diff[i] == True:
        continue
    elif diff[i] == False:
        diff[i] = True
        diff[i + 1] = True
        ans += 1

print(ans)