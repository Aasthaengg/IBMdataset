# coding: utf-8
# Your code here!

A=input()

A=list(map(lambda x:ord(x)-97,A))

log=[0]*26
log[A[0]]+=1
ans=1


for i in range(1,len(A)):
    ans+=i-log[A[i]]
    log[A[i]]+=1

print(ans)