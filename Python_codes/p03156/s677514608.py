N=int(input())
A,B=map(int,input().split())
P=list(map(int,input().split()))
a=0
b=0
c=0
for num in P:
    if num<=A:
        a+=1
    elif A<num<=B:
        b+=1
    else:
        c+=1

print(min(a,b,c))