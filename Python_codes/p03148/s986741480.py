from collections import Counter
import sys
INF = 10 ** 18
def LI(): return [int(x) for x in sys.stdin.readline().split()]
def MI(): return map(int, sys.stdin.readline().split())


N, K = MI()
# 美味しさ降順寿司
sushi = sorted([LI() for _ in range(N)], key=lambda x:x[1], reverse=True)
# 美味しい寿司を貪欲に取る
delicious_sushi = sushi[:K]
# 余った寿司
soudemonai_sushi = sushi[K:]

syurui_counter = Counter()
deliciousness = 0

f = [-INF for _ in range(K+1)]

for x in delicious_sushi:
    syurui_counter[x[0]] += 1
    deliciousness += x[1]

f[len(syurui_counter)] = deliciousness

# print(delicious_sushi)
# print(soudemonai_sushi)
# print(syurui_counter)
# print("==========")

delicious_sushi = delicious_sushi[::-1]

i = 0
j = 0
while len(syurui_counter) < K and 0 < len(soudemonai_sushi):
    # print("len(syurui_counter) = " + str(len(syurui_counter)))
    while i < K:
        # print("i = " + str(i))
        if syurui_counter[delicious_sushi[i][0]] >= 2:
            # print(delicious_sushi[i])
            break
        i += 1
    while j < N - K:
        # print("j = " + str(j))
        if syurui_counter[soudemonai_sushi[j][0]] == 0:
            # print(soudemonai_sushi[j])
            break
        j += 1
    if j == N - K:
        break
    deliciousness -= delicious_sushi[i][1]
    deliciousness += soudemonai_sushi[j][1]
    syurui_counter[delicious_sushi[i][0]] -= 1
    syurui_counter[soudemonai_sushi[j][0]] += 1
    # print(syurui_counter)
    f[len(syurui_counter)] = deliciousness
    i += 1
    j += 1
    # print("==========")

# print(f)
for i in range(len(f)):
    f[i] += (i * i)
# print(f)
print(max(f))
