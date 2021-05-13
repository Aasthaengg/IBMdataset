from itertools import permutations
n,a,b,c=map(int,input().split())
target=[a,b,c]
lst=[int(input()) for _ in range(n)]
p=list(permutations(lst,3))
ans=float("inf")

def Base_10_to_n(X, n,keta):
    X_dumy = X
    out = ''
    while X_dumy>0:
        out = str(X_dumy%n)+out
        X_dumy = int(X_dumy/n)
    out="0"*(keta-len(out))+out
    return out
for q in range(len(p)):
    base_tri=list(p[q])
    extra=lst[:]
    for i in base_tri:
        extra.remove(i)
    tmp=0
    for i in range(3):
        tmp+=abs(base_tri[i]-target[i])
    ans=min(tmp,ans)
    for i in range(1,4**(n-3)):
        tmp=0
        tri=base_tri[:]
        yonshin=Base_10_to_n(i,4,n-3)
        for j in range(n-3):
            if yonshin[j]=="1":
                tri[0]+=extra[j]
                tmp+=10
            elif yonshin[j]=="2":
                tri[1]+=extra[j]
                tmp+=10
            elif yonshin[j]=="3":
                tri[2]+=extra[j]
                tmp+=10
        for j in range(3):
            tmp+=abs(tri[j]-target[j])
        ans=min(tmp,ans)
print(ans)