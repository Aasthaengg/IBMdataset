n=int(input())
L=list(map(int,input().split()))
LL=list(set(L))
ans="No"
if LL==[0]:
    ans="Yes"
elif len(LL)==2:
    if L.count(LL[0])==2*L.count(LL[1]) or L.count(LL[1])==2*L.count(LL[0]):
        ans="Yes"
elif len(LL)==3:
    if L.count(LL[0])==L.count(LL[1]) and L.count(LL[1])==L.count(LL[2]):
        if LL[0]^LL[1]^LL[2]==0:
            ans="Yes"
print(ans)