n = int(input())
a = list(map(int, input().split()))
M=max(a)
biggest_prime = [0] * (M+10)
for i in range(2, M+10):
    if biggest_prime[i] == 0:
        biggest_prime[i] = i
        for j in range(i*i, M+1, i):
            biggest_prime[j] = i

from collections import defaultdict
cntd=defaultdict(int)
for i in range(len(a)):
    num = a[i]
    while num>1:
        p=biggest_prime[num]
        cntd[p]+=1
        while num % p == 0:
            num//=p

flg=False
for c in cntd.values():
    if c==n:
        print("not coprime")
        exit()
    if c>1:
        flg=True
if flg:
    print("setwise coprime")
else:
    print("pairwise coprime")