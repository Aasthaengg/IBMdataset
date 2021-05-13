import sys
import numpy as np
input = sys.stdin.readline

N,K = list(map(int,input().split()))
p = np.array(list(map(int,input().split())))

pn1 = p - 1

ans = sum(pn1[:K])
spb = ans
for i in range(N-K):
    sp = spb -pn1[i] + pn1[i+K]
    #print(sp,spb,pn1[i],pn1[i+K])
    ans = max(sp,ans)
    spb = sp
print(ans/2+K)

