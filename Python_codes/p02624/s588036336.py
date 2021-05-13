from math import floor
N = int(input())
ans = 0
# for j in range(1, N+1):
#     for i in range(1, N+1):
#         if i % j == 0: # iがjの倍数なら
#             ans += i
for j in range(1, N+1):
    n = N//j
    ans += j*n*(n+1)//2
print(ans)