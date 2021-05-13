N=int(input())
a=[int(input())for i in range(N)]
p=1
ok=False
ans=0
for i in range(N):
    if p==2:
        ok=True
        break
    p=a[p-1]
    ans+=1
print(ans if ok else -1)