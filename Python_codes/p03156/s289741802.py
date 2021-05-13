N=int(input())
A,B=map(int,input().split())
P=list(map(int,input().split()))
l=[0,0,0]
for i in P:
    if i<=A:
        l[0]+=1
    elif i<=B:
        l[1]+=1
    else:
        l[2]+=1
print(min(l))