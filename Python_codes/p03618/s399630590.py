A=list(input())
n=len(A)
ind=[[] for i in range(26)]
for i in range(n):
    ind[ord(A[i])-97].append(i)
cnt=0
for i in range(26):
    cnt+=len(ind[i])*(len(ind[i])-1)//2

print(n*(n-1)//2-cnt+1)