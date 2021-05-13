n=int(input())
a1=list(map(int,input().split()))
a2=list(map(int,input().split()))
ans=0
for i in range(n):
    top=sum(a1[:i+1])
    bottom=sum(a2[i:])
    tmp=top+bottom
    ans=max(tmp,ans)
print(ans)