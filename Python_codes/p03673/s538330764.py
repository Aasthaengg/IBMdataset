n=int(input())
a=list(map(int,input().split()))

left=[]
right=[]
if n%2!=0:
    for i in range(0,n,2):
        left.append(a[n-i-1])
    for i in range(1,n,2):
        right.append(a[i])
else:
    for i in range(0,n,2):
        left.append(a[n-i-1])
    for i in range(0,n,2):
        right.append(a[i])


ans=left
ans.extend(right)
L=[str(a) for a in ans]
L=" ".join(L)
print(L)
