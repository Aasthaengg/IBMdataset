from collections import Counter
# ABC159 D

N=int(input())
A=list(map(int,input().split()))

c=Counter(A)
res=[]
for p,r in c.items():
    res.append((r*(r-1))//2)
sum_res=sum(res)
for k in range(N):
    r=c[A[k]]
    print(sum_res-(r*(r-1))//2+((r-1)*(r-2))//2)