ma = lambda :map(int,input().split())
lma = lambda :list(map(int,input().split()))
tma = lambda :tuple(map(int,input().split()))
ni = lambda:int(input())
yn = lambda fl:print("YES") if fl else print("NO")
import collections
import math
import itertools
import heapq as hq
n,k  = ma()
A  = lma()
mx = max(A)
lm = len(bin(max(mx,k)))-2
ls = [0]*lm
for a in A:
    ba = bin(a)[::-1]
    for i in range(len(ba)-2):
        if ba[i]=="1":
            ls[i]+=1

bk = bin(k)[2:].zfill(lm)
bk=bk[::-1]
lk = len(bk)
def score(idx,f2=False):
    f=False
    ret=0
    if bk[idx]=="1":
        f=True
    for i in range(lm):
        if f2:
            if bk[i]=="0":
                ret+=ls[i]*2**i
            else:
                ret+=max(ls[i],n-ls[i])*2**i
            continue
        if f:
            if i<idx:
                ret+=max(ls[i],n-ls[i])*2**i
            elif i==idx:#bk[i]==0
                ret +=ls[i]*2**i
            else:
                if bk[i]=="0":
                    ret+=ls[i]*2**i
                else:
                    ret+=max(ls[i],n-ls[i])*2**i
        else:
            if bk[i]=="0":
                ret+=ls[i]*2**i
            else:
                ret+=max(ls[i],n-ls[i])*2**i

    return ret
ans = 0
for i in range(1,lk):
    tmp = score(i)
    #print(tmp)
    ans = max(ans,tmp)
ans = max(ans,score(0,f2=True))
print(ans)
#bina = [bin(a)[2:] for a in A]; print(*bina)
#print(ls)
# print(bin(k)[2:],bk)
