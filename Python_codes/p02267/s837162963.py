n=int(input())
l1=list(map(int,input().split()))
m=int(input())
l2=list(map(int,input().split()))
c=0
for i in l2:
    if i in l1:
        c+=1
print(c)
