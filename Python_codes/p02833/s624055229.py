n = int(input())

# Lv.1
#def f(t):
#    return 1 if t < 2 else t * f(t-2)
#print(f(n))

# Lv.2
# def g(p):
#     d = {2:0, 5:0}
#     for i in range(p, 1, -2):
#         t = i
#         while(t % 2 == 0):
#             t //= 2
#             d[2] += 1
#         while(t % 5 == 0):
#             t //= 5
#             d[5] += 1
#     return min(d[2], d[5])
# print(g(n))

# Lv.3
# 1,3,5,7,... 末尾は奇数
# 2,4,6,8,... Lv.2 の print(min(d[2], d[5])) は 5の方が常にmin
# 100 の時 10 で割れるのが10, 50で割れるのが2つ
# 250 の時 10 で割れるのが25, 50で割れるのが5つ, 250 で割れるのが1つ 1000個位出してみたら ? 整数分割の + - 交互のあれでは無いっぽい
k = 10
ans = 0
while k <= n:
    ans += n // k
    k = k * 5
print(ans if n % 2 == 0 else 0)