from collections import Counter
n = int(input())
A = list(map(int,input().split()))
mod = 10**9 + 7
c = Counter(A)
flg = True
for k,v in c.items():
    if k==0:
        if v!=1:
            flg = False
    else:
        if v!=2:
            flg = False
if flg is False:
    print(0)
else:
    print(pow(2, n//2, mod))