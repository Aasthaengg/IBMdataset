import math as m

def isltK(K,X):
    ccut=0
    for Ai in As:
        ccut += m.ceil(Ai/X)-1
    if ccut <=K:
        return True
    else:
        return False


N,K=map(int,input().split())
As=list(map(int,input().split()))

l=1
h=max(As)
while l < h:
    mid = (l+h)//2
    if isltK(K,mid):
        h=mid
    else:
        l=mid+1
print(l)