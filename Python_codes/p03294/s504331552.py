import numpy as np
N = int(input())
a = list(map(int,input().split()))

# t = np.lcm.reduce(a)
ans = 0
# for i in a:
#     ans = ans + (t-1) % i
# print(a)
# print(ans)

ans = sum(a) - N
print(ans)