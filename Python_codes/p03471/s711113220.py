n,y=map(int,input().split())
y//=1000
res=False
ans=["-1","-1","-1"]
for i in range(n+1):
    for j in range(n+1-i):
        if 10*i+5*j+(n-i-j)==y:
            ans=[str(i),str(j),str(n-i-j)]
            res=True
            break
    if res:
        break

print(" ".join(ans))
