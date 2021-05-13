N,*A=map(int, open(0).read().split())
A=sorted(A)
ans=1
acc=0
for a in A:
    if a>acc*2:
        ans=1
    else:
        ans+=1
    acc+=a
print(ans)