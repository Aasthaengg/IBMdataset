# coding: utf-8
A,B=map(int, input().split())
ans=[]
if A>B:
    ans.append(A)
    A-=1
else:
    ans.append(B)
    B-=1

if A>B:
    ans.append(A)
else:
    ans.append(B)
    
print(sum(ans))