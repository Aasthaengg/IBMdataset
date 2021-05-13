memo = {}
def f(m,k):
    if k>m:
        return 0
    if m==1:
        return 1
    if k==0:
        return 1
    if k==1:
        return m
    if (m,k) in memo:
        return memo[(m,k)]
    memo[(m,k)]=f(m-1,k-1)+f(m-1,k)
    return memo[(m,k)]

N,A,B = map(int,input().split())
V = sorted(list(map(int,input().split())),reverse=True)
amin = 10**15+10
for i in range(A):
    amin = min(amin,V[i])
av = sum(V[:A])/A
cnt = 0
for i in range(N):
    if V[i]==amin:
        cnt += 1
cntB = 0
for i in range(B):
    if V[i]==amin:
        cntB += 1
cntA = 0
for i in range(A):
    if V[i]==amin:
        cntA += 1
print(av)
if V[0]>amin:
    print(f(cnt,cntA))
else:
    tot = 0
    for i in range(cntA,cntB+1):
        tot += f(cnt,i)
    print(tot)