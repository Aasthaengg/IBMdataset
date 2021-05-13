N=int(input())
A,B=map(int,input().split())
P=list(map(int,input().split()))
l=[0,0,0]

for i in range(N):
    if P[i]<=A:
        l[0]=l[0]+1
    elif P[i]<=B:
        l[1]=l[1]+1
    else:
        l[2]=l[2]+1
print(min(l))