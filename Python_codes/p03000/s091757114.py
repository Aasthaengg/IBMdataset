N,X=map(int,input().split())

list1=list(map(int,input().split()))
a=0
ans=1

for i in range(N):
    a=a+list1[i]
    if a<=X:
        ans+=1
        
print(ans)
