N=int(input())
A,B=map(int,input().split())
P=list(map(int,input().split()))
a=0
ab=0
b=0
for i in range(N):
    if P[i]<=A:
        a+=1
    elif A+1<=P[i] and P[i]<=B:
        ab+=1
    else:
        b+=1
C=[a,ab,b]
print(min(C))