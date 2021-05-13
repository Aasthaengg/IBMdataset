from itertools import accumulate

n, k = map(int, input().split())
A = list(map(int, input().split()))
A.sort(reverse=True)
goukei = sum(A)


# 約数列挙
def divide(n):  # unsort
    ans = []
    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0:
            ans.append(i)
            if n // i == i:
                continue
            ans.append(n // i)
    return ans


kouho = divide(goukei)
kouho.sort(reverse=True)
ans = 0
for num in kouho:
    delta = 0
    outflag = 0
    d = [0] * n
    for i in range(n):
        d[i] = A[i] % num
    d.sort()
    SD = list(accumulate([0] + d))
    for i in range(n + 1):
        sageru = SD[i]
        ageru = num * (n - i) - (SD[n] - SD[i])
        delta = ageru - sageru
        if delta % num == 0 and max(sageru, ageru) <= k:
            print(num)
            exit()
print(1)
