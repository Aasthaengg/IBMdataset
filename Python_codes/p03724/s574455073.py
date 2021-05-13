n,m=map(int,input().split())
l=[0]*n
for i in range(m):
    a,b=map(int,input().split())
    l[a-1]+=1
    l[b-1]+=1
k=0
while k<n:
    if l[k]%2==0:
        k+=1
        continue
    else:
        print("NO")
        exit()
print("YES")