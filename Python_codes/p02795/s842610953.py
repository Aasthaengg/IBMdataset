H=int(input())
W=int(input())
N=int(input())
c=0
ans=0
if H>=W:
    while c>=0:
        c+=H
        ans+=1
        if c>=N:
            break
else:
    while c>=0:
        c+=W
        ans+=1
        if c>=N:
            break
print(ans)