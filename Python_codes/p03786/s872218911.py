import numpy as np 
n = int(input())
size_ls = list(map(int, input().split()))
size_ls.sort()
csum_size = list(np.cumsum(size_ls))

can_ls = [0] * n
can_ls[-1] = 1
for i in range(n-1):
    if 2 * csum_size[i] >= size_ls[i+1]:
        can_ls[i] = 1
ans = 0
for i in range(n-1,-1,-1):
    if can_ls[i] != 1:
        break
    ans += 1
print(ans)

