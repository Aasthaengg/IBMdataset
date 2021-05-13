N, K = map(int, input().split())

"""
2(a+b+c) = nK <= 6N
n=1,2,......,6N//K

a+b=iK-c<=2
2N>=iK-c

a+c=iK
a+b=jK
b-c=XK Xは整数
b+c=kK kは自然数
2b=(X+k)K 
b=X'K/2
→K=2a：bはa刻み
→K=2a-1：bはK刻み
"""


# max_n = (2*N)//K
# count = 0
# anslist = []
# for sum_ab in range(K, 2*N + 1, K):
#     print(("a+b", sum_ab))
#     min_a = sum_ab - N if sum_ab - N >= 1 else 1

#     for a in range(min_a, min(sum_ab, N+1)):
#         b = sum_ab - a
#         if (a - b) % K != 0:
#             continue
#         if b < 1 or b > N:
#             break
#         lower = min(a, b)
#         for c in range(1, N+1):
#             if (lower + c) % K == 0:
#                 # print((a, b, c))
#                 anslist.append([a, b, c])
#                 count += 1
# anslist.sort(key=lambda x: x[0])
# print(anslist)
# print(count)

if K % 2 == 0:
    kizami = K // 2
    max_kizami = N // kizami
    pa1 = max_kizami // 2
    pa2 = max_kizami - pa1
    print(pa1**3+pa2**3)
else:
    kizami = K
    max_kizami = N // kizami
    print(max_kizami**3)

"""偶数の場合
a+b=K max_kizami通り
    kizami kizami [kizami,kizami+K,...]
a+b=2K 2max_kizami　+　N//K通り
    1kizami 3kizami [kizami,kizami+K,...]
    2kizami 2kizami [2kizami,4kizami,...]
    3kizami 1kizami [kizami,kizami+K,...]


a+b=2(N//K)K
    max_kizami*kizami max_kizami*kizami [kizami,...]
"""
"""奇数の場合
K K [K,2K,...]

2K K []
K 2K []

3K K []
2K 2K []
K 3K []



max_kizami
"""
