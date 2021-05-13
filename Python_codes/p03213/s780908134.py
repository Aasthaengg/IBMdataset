n = int(input())

from math import factorial
def comb(n, r):
    if n < r:
        return 0
    return factorial(n) // factorial(r) // factorial(n - r)

def factorization(n):
    arr = []
    temp = n
    for i in range(2, int(-(-n**0.5//1))+1):
        if temp%i==0:
            cnt=0
            while temp%i==0:
                cnt+=1
                temp //= i
            arr.append([i, cnt])

    if temp!=1:
        arr.append([temp, 1])

    if arr==[]:
        arr.append([n, 1])

    return arr

d = {}

for i in range(1, n+1):
    for m, cnt in factorization(i):
        if m == 1:
            continue
        if m in d:
            d[m] += cnt
        else:
            d[m] = cnt

cnt = [0 for i in range(100)]

for k in d:
    cnt[d[k]] += 1

print(
    sum(cnt[74:]) + # 75
    sum(cnt[4:14]) * sum(cnt[14:]) + sum(cnt[14:]) * (sum(cnt[14:])-1) + # 5 * 15
    sum(cnt[2:24]) * sum(cnt[24:]) + sum(cnt[24:]) * (sum(cnt[24:])-1) + # 3 * 25
    sum(cnt[2:4]) * comb(sum(cnt[4:]), 2) + sum(cnt[4:]) * comb(sum(cnt[4:])-1, 2) # 3 * 5 * 5
)
