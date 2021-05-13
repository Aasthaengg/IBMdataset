def ncr(n, r):
    if n < r: return 0
    r = min(r, n - r)
    if r == 0: return 1
    if r == 1: return n
    numerator = [n - r + i + 1 for i in range(r)]
    denominator = [i + 1 for i in range(r)]
    for p in range(2, r + 1):
        pivot = denominator[p - 1]
        if pivot > 1:
            offset = (n - r) % p
            for k in range(p - 1, r, p):
                numerator[k - offset] /= pivot
                denominator[k] /= pivot
    result = 1
    for k in range(r):
        if numerator[k] > 1:
            result *= numerator[k]
    return int(result)


n, p = map(int, input().split())
a = list(map(int, input().split()))
# ans = 0
# for maskN in range(1 << n):
#     # print(maskN)
#     tmp = 0
#     for i in range(n):
#         if (maskN >> i & 1 == 1):
#             tmp += a[i]
#     if tmp % 2 == p:
#         ans += 1

# print(ans)

dic = {'odd': 0, 'even': 0}

for i in a:
    if i % 2 == 0:
        dic['even'] += 1
    else:
        dic['odd'] += 1

even = 0
odd = 0
# 偶数個の組み合わせ総数
for i in range(dic['even'] + 1):
    even += ncr(dic['even'], i)

if p == 0:
    for i in range(0, dic['odd'] + 1, 2):
        odd += ncr(dic['odd'], i)

else:
    for i in range(1, dic['odd'] + 1, 2):
        odd += ncr(dic['odd'], i)

print(odd * even)
