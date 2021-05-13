from scipy.misc import comb #<-Atcoderではこちらを使うべし


def factorization(n):
    arr = []
    temp = n
    for i in range(2, int(-(-n**0.5 // 1)) + 1):
        if temp % i == 0:
            cnt = 0
            while temp % i == 0:
                cnt += 1
                temp //= i
            arr.append([i, cnt])
    if temp != 1:
        arr.append([temp, 1])
    if arr == []:
        arr.append([n, 1])
    return arr


ans = 1
n, m = map(int, input().split())
lst = factorization(m)
if lst[0][0] == 1:
    print(1)
    exit()
for e in lst:
    ans *= comb((n + e[1] - 1), n - 1, exact=True)
print(ans % 1000000007)
