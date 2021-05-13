n=int(input())
l=list(map(int,input().split()))
max=max(l)
cnt=0
c=0
for i in range(n):
    if l[i]==max and cnt==0:
        cnt+=1
    else:
        c+=l[i]
if max<c:
    print("Yes")
else:
    print("No")
