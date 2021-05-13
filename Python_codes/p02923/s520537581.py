N=int(input())
H=[int(x) for x in input().split()]
ans=0
cur=0
for i,h in enumerate(H):
    if i>=1 and h<=H[i-1]:
        cur=cur+1
        ans=max(ans,cur)
    else:
        cur=0
print(ans)
