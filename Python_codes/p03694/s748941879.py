N=int(input())
L=list(map(int,input().split()))
M=sorted(list(set(L)))
ans=0
for i in range (len(M)-1):
  ans+=M[i+1]-M[i]
print(ans)