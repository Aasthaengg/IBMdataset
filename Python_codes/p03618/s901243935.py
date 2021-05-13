from collections import defaultdict
s=input()
N=len(s)
D=defaultdict(int)
for i in range(N):
  D[s[i]]+=1
ans=N*(N-1)//2
for d in D.values():
  ans-=d*(d-1)//2
print(ans+1)