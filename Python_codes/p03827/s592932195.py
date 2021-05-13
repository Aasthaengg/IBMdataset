n=int(input())
s=input()
S=len(s)
x=0
X=0
for i in range(S):
    if s[i]=="I":
        x+=1
        if X<x:
            X=x
        
    else:
        x-=1

print(X)