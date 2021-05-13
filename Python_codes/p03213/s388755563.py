import sys
input = sys.stdin.readline

n = int(input())

def factorization(n):
    arr = []
    temp = n
    for i in range(2, int(-(-n**0.5//1)) + 1):
        if temp%i==0:
            cnt = 0
            while temp%i==0:
                cnt += 1
                temp //= i
            arr.append([i, cnt])
    if temp!=1:
        arr.append([temp, 1])
    
    if arr ==[]:
        arr.append([n, 1])
    
    return arr

from collections import defaultdict

d = defaultdict(int)

for i in range(2, n + 1):
    arr = factorization(i)
    for j in arr:
        d[j[0]] += j[1]
v = d.values()

from collections import Counter

c = Counter(v)
li = [0]*5

for i in c.keys():
    if i >= 2:
        li[0] += c[i] # 2
    if i >= 4:
        li[1] += c[i] # 4
    if i >= 14:
        li[2] += c[i] # 14
    if i >= 24:
        li[3] += c[i] # 24
    if i >= 74:
        li[4] += c[i] # 74

ans = 0
ans += li[1] * (li[1] - 1) // 2 * (li[0] - 2)
ans += li[2] * (li[1] - 1)
ans += li[3] * (li[0] - 1)
ans += li[4]

print(ans)