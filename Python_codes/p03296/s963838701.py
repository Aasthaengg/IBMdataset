n=int(input())
l=list(map(int,input().split()))
l.append(10000000)
ans=0
f=1
for i in range(n):
    if l[i]==l[i+1]:
        f+=1
    else:
        ans+=f//2
        f=1
print(ans)