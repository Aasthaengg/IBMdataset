import numpy as np
n, k=map(int, input().split())
a=list(map(int, input().split()))

lst=[0]*(max(a)+1)
for i in a:
    lst[i]+=1

ruiseki=[0]*(max(a)+1)
for i,j in enumerate(lst):
    ruiseki[i] = ruiseki[i-1]+j
sm1=0
for i in a:
    sm1 += ruiseki[i-1]

ans1=(((k*(k-1))//2)%(10**9+7))*sm1

npr=np.array(ruiseki)
sm2=0
for i in a:
    sm2 += npr[i-1]
    npr[i:] -= 1

ans2=(sm2*k)%(10**9+7)
ans=(ans1+ans2)%(10**9+7)

print(ans)