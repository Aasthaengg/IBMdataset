N=int(input())
S=input()
x=0
ans=0
for i in S:
    if i=='I':
        x+=1
    else:
        x+=-1
    if ans<x:
        ans=x
print(ans)
