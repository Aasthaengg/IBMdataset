n=int(input())
l1=list(map(int,input().split()))
l2=list(map(int,input().split()))
v=0
for i in range(n):
    if l1[i]-l2[i]>0:
        v+=l1[i]-l2[i]
print(v)