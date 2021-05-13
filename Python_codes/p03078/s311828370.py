x,y,z,k=map(int,input().split())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
c=list(map(int,input().split()))

ab=[]

for aa in a:
    for bb in b:
        ab.append(aa+bb)

ab.sort(reverse=True)

abk=ab[:k]

ans=[]

for item in abk:
    for cc in c:
        ans.append(item+cc)

ans.sort(reverse=True)

for item in ans[:k]:
    print(item)
