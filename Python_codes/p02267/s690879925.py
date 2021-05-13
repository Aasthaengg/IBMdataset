# coding: utf-8
# Your code here!
n=int(input())
S=list(map(int,input().split()))
S1=set(S)


q=int(input())
T=list(map(int,input().split()))
count=0

for j in range(q):
    if T[j] in S1:
        count+=1
    
        
print(count)
