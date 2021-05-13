n=int(input())
flag=0
ans=[]
cnt=0
if n%2==0:flag=1
for i in range(1,n):
    for j in range(i+1,n+1):
        if i+j!=n+flag:
            cnt+=1
            ans.append([i,j])
print(cnt)
for i in ans:
    print(*i)