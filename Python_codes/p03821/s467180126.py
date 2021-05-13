n=int(input())
a=[];b=[]
for i in range(n):
    A,B=map(int,input().split())
    a.append(A)
    b.append(B)
k=0
ans=0
for i in range(n-1,-1,-1):
    if (a[i]+ans)%b[i]==0:
        continue
    ans += b[i]-((a[i]+ans)%b[i])
print(ans)