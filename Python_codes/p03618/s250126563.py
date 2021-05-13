S=input()
A=[0]*26
N=len(S)
a=ord('a')
ans=0
for i in range(N):
    t=ord(S[i])-a
    A[t]+=1
for t in range(26):
    ans+=(A[t]*(A[t]+1))//2
print((N*(N+1))//2 - ans +1)