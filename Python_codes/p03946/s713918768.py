from collections import defaultdict

N,T=map(int,input().split())
A=list(map(int,input().split()))

m=A[N-1]
maxlist=[A[N-1]]
for i in range(1,N):
    a=A[-i-1]
    m=max(m,a)
    maxlist.append(m)

maxlist=maxlist[::-1]

benefit=defaultdict(int)

for i in range(0,N-1):
    b=-A[i]*(T//2)+maxlist[i+1]*(T//2)
    benefit[b]+=1

ans=0
for key in benefit.keys():
    if benefit[key]>0 and key>ans:
        ans=key

print(benefit[ans])