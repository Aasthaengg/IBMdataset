from collections import Counter

N,M=map(int,input().split())
A=list(map(int,input().split()))

B=[0]
for Ai in A:
    B.append((B[-1]+Ai)%M)

C=Counter(B)
v=dict(C).values()
ans=sum([x*(x-1)//2 for x in v])

# print(B)
# print(C)
# print(v)
print(ans)