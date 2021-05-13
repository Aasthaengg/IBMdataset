N=input()
S=list(input())
x=0
l=list()
for i in S:
    if i=='I':
        x+=1
    else:
        x-=1
    l.append(x)
n=max(l)
print(max(0,n))