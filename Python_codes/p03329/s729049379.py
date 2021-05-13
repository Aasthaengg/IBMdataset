import copy
n = int(input())
# cur = n
# ans = 0
# while cur >= 6:
#     div6 = 0
#     a = copy.deepcopy(cur)
#     while a != 0:
#         a //= 6
#         div6 += 1
#     div9 = 0
#     b = copy.deepcopy(cur)
#     while b != 0:
#         b //= 9
#         div9 += 1
#     div6 -= 1
#     div9 -= 1
#     if 6**div6 > 9**div9:
#         cur -= 6**div6
#     else:
#         cur -= 9**div9
#     ans += 1
#     print(cur)
# print(ans + cur)

dp = [0]*(n+1)
moto = []
a = 1
while a <= n:
    a *= 6
    if a <= n:
        moto.append(a)
a = 1
while a <= n:
    a *= 9
    if a <= n:
        moto.append(a)

for i in range(1, n+1):
    tar = [dp[i-1]+1]
    for j in moto:
        if i >= j:
            tar.append(dp[i-j]+1)
    dp[i] = min(tar)
print(dp[n])




