N=list(map(int,input().split()))
N.sort()
co=[1,4,7,9]

ans="YES"
for i in range(4):
    if N[i]!=co[i]:
        ans="NO"
        break
        
print(ans)