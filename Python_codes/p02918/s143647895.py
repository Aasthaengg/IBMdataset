n,k=map(int,input().split())
a=list(input())
count=0
for i in range(n):
    if a[i]=="L" and i-1>=0 and a[i-1]=="L":
        count+=1
    elif a[i]=="R" and i+1<=n-1 and a[i+1]=="R":
        count+=1
print(min(n-1,count+k*2))