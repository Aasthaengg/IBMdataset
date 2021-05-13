n=int(input())
p=list(map(int,input().split()))
ans=0
for i in range(n-2):
    if (p[i+1]<p[i] and p[i+1]<p[i+2]) or (p[i+1]>p[i] and p[i+1]>p[i+2]):
        pass
    else:
        ans+=1
print(ans)