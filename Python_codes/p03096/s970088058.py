#B
import sys
input=sys.stdin.readline
sys.setrecursionlimit(10**9)
mod=10**9+7
n=int(input())
C=[int(input()) for _ in range(n)]
A=[0]*(2*10**5+1) #A[i]:色iが最後にあった場所(1-indexed)
B=[1]
for i,c in enumerate(C):
    #print(A[c])
    tmp=B[-1]
    if A[c]!=i and A[c]!=0:
        tmp+=B[A[c]]
    A[c]=i+1
    B.append(tmp%mod)
#print(B)
print(B[-1])