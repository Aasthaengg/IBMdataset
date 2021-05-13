N=int(input())
S,T=map(str,input().split())
X=[0]*N
for i in range(N):
  X[i]=S[i]+T[i]
print("".join([str(i) for i in X]))