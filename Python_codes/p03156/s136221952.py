N=int(input())
A,B=map(int,input().split())
p=list(map(int,input().split()))
No1=No2=No3=0

for i in p:
    if i <= A:
        No1 += 1
    elif i >= A and i <= B:
        No2 += 1
    else:
        No3 += 1

print(min(No1,No2,No3))
