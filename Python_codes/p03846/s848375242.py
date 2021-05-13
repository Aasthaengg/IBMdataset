from collections import Counter
n = int(input())
a = list(map(int, input().split()))
mod = 10**9+7
flag = True
c = Counter(a)
#print(c)
if n % 2 == 1:
    if c[0] != 1:
        flag = False
    for i in range(1, n//2+1):
        if c[i*2] != 2:
            flag = False
            break
    if flag:
        print(2**(n//2) % mod)
    else:
        print(0)
elif n % 2 == 0:
    for i in range(n//2):
        if c[i*2+1] != 2:
            flag = False
            break
    if flag:
        print(2**(n//2) % mod)
    else:
        print(0)