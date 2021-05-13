n=int(input())
A=[int(i) for i in input().split()]
B=[int(i) for i in input().split()]
C=[int(i) for i in input().split()]

A.sort()
B.sort()
C.sort()

A.append(10**10)
B.append(10**10)
C.append(10**10)

btab=[0 for i in range(n)]

idx=0
for i in range(n):
    while A[idx] < B[i]:
        idx+=1
    btab[i]=idx

idx=0
sow=0
ans=0
for i in range(n):
    while B[idx] < C[i]:
        sow+=btab[idx]
        idx+=1
    ans+=sow

print(ans)