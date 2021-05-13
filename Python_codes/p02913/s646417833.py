n = int(input())
s = input()

import random
base1 = 1007
mod1 = 10**9+7
modTank1 = [3000012541,3000012553,3000012563,3000012649,3000012683,3000012709]
mod1 = modTank1[random.randint(0,5)]
base1 = 1007
mod1 = 10**9+7
hash1 = [0]*(n+1)
power1 = [1]*(n+1)
for i,e in enumerate(s):
    hash1[i+1] = (hash1[i]*base1 + ord(e))%mod1
    power1[i+1] = (power1[i]*base1)%mod1
def rolling_hash(i, j):
    return (hash1[j]-hash1[i]*power1[j-i]%mod1)%mod1



hash = set()
l = 0
r = n
while r - l > 1:
    m = l + (r-l)//2
    hash = dict()
    flag = 0
    for i in range(n-m+1):
        h = rolling_hash(i, i+m)
        if h not in hash.keys():
            hash[h] = i
        elif hash[h]+m <= i:
            flag = 1
            break
    if flag == 1:
        l = m
    else:
        r = m

print(l)
