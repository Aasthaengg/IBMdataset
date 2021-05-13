import sys
def input():
    return sys.stdin.readline()[:-1]
N=int(input())
pr=10**9+7
a=0
l=[0]*(2*10**5)
C=[int(input())-1 for i in range(N)]
for i in range(N-1):
    if C[i]==C[i+1]:
        continue
    a,l[C[i]]=(l[C[i]]+a)%pr,(l[C[i]]+a+1)%pr
a+=l[C[-1]]
print((a+1)%pr)