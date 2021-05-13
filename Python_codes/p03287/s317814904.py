# coding: utf-8
# Your code here!
N,M=map(int,input().split())

A=list(map(int,input().split()))

A=list(map(lambda x:x%M,A))

dic={}
dic[0]=1

ans=0
temp=0

for i in range(len(A)):
    temp+=A[i]
    
    if temp%M in dic:
        ans+=dic[temp%M]
        dic[temp%M]+=1
    else:
        dic[temp%M]=1
    #print(ans)
#print(dic)
print(ans)