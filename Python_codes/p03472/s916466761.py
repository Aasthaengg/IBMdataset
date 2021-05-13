N,H=map(int,input().split())
As=[]
Bs=[]
for _ in range(N):
    a,b=map(int,input().split())
    As.append(a)
    Bs.append(b)
ans=0
max_a=max(As)
sort_Bs=sorted(Bs,reverse=True)
new_Bs=[]
for b in sort_Bs:
    if b>max_a:
        new_Bs.append(b)
for b in new_Bs:
    H-=b
    ans+=1
    if H<=0:
        break
if H>0:
    if H%max_a==0:
        ans+=(H//max_a)
    else:
        ans+=(H//max_a+1)
print(ans)
