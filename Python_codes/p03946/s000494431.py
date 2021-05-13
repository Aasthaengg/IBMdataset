# D - 高橋君と見えざる手
# https://atcoder.jp/contests/abc047/tasks/arc063_b

from collections import Counter
N,T=map(int,input().split())
A=list(map(int,input().split()))

mini=10**9
maxi=0
m = [0]*N
M = [0]*N
z = [0]*N
for i in range(N):
    mini=min(mini,A[i])
    maxi=max(maxi,A[i])
    m[i]= mini
    M[i]= maxi
    z[i]= A[i]-mini
k=Counter(z)
l=sorted(k,reverse=True)
#print(l)
print(k[l[0]])