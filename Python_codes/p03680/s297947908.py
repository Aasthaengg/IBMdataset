n=int(input())
a=[]
for i in range(n):
    a.append(int(input()))

ans=0
j=0
for i in range(n):
    ans+=1
    if i==0:
        j=a[i]
    if j==2:
        print(ans)
        exit()
    j=a[j-1]
print(-1)
